from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent
from messages.schema import ChatRequest


app = FastAPI()

@app.post("/chat")
async def chat_with_manny(request: ChatRequest):

    user_message = request.message.strip()
    response, name, role = run_agent(user_message)

    return {
        "response": response,
    }