from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.message

    # Simple AI logic (replace this with powerful AI logic or model)
    if "hello" in user_message.lower():
        reply = "Hello! How can I help you today?"
    elif "your name" in user_message.lower():
        reply = "I'm NeuraMind AI, your personal assistant."
    else:
        reply = f"You said: {user_message}"

    return {"reply": reply}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)