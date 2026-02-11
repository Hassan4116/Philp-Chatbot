
from fastapi import APIRouter
from app.schemas import chatRequest, chatResponse
from app.services.openai_service import get_philp_reply
from app.routes.router import detect_mode

router = APIRouter()

@router.post("/chat", response_model=chatResponse)
def chat_with_philp(req: chatRequest):
    mode = detect_mode(req.message)

    reply = get_philp_reply(
        req.message, 
        req.session_id, 
        mode)
    return chatResponse(reply=reply, mode=mode)