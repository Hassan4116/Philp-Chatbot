from fastapi import APIRouter
from app.schemas import chatRequest, chatResponse
from app.services.openai_service import get_philp_reply
from app.routes.router import detect_mode_and_language
from app.services.safety import is_safe
from app.services.rag import handle_rag

router = APIRouter()

@router.post("/chat", response_model=chatResponse)
def chat_with_philp(req: chatRequest):
    mode_and_language = detect_mode_and_language(req.message)
    mode = mode_and_language["mode"]
    language = mode_and_language["language"]
    # Safety first
    if not is_safe(req.message, language):
        return chatResponse(reply="I cannot respond to violent or harmful statements. Let's keep the conversation safe.", mode="general")

    if mode == "rag":
        reply = handle_rag(req.message, req.session_id, language)
    else:
        reply = get_philp_reply(
            req.message, 
            req.session_id, 
            mode,
            language)
        
    return chatResponse(reply=reply, mode=mode)