# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

# Connect to local vLLM server
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

app = FastAPI(title="Chatbot API")

# Allow frontend to call
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model="/home/coolder/.cache/modelscope/hub/models/Qwen/Qwen3-0.6B",
        messages=[{"role": "user", "content": req.message}]
    )
    print(response)
    # Access the response content using the correct attribute access
    return {"response": response.choices[0].message.content}
