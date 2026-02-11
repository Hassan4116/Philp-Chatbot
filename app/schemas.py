from pydantic import BaseModel

class chatRequest(BaseModel):
    message: str
    session_id: str

class chatResponse(BaseModel):
    reply: str