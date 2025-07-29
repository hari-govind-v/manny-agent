from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    name: str
    role: str
