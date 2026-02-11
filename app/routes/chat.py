
from fastapi import APIRouter
from app.schemas import chatRequest, chatResponse
from app.services.openai_service import get_philp_reply

router = APIRouter()

@router.post("/chat", response_model=chatResponse)
def chat_with_philp(req: chatRequest):
    reply = get_philp_reply(req.message, req.session_id)
    return chatResponse(reply=reply)