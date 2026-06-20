from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.request import ChatRequest
from app.models.response import ChatResponse

from app.core.config import DATA_PATH
from app.services.data_loader import DataLoader
from app.core.chatbot import SoccerChatbot

app = FastAPI(title="Football AI Chatbot", version="1.0.0")


# Allow HTML frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load match data once
data_loader = DataLoader(DATA_PATH)

chatbot = SoccerChatbot(data_loader.data)


@app.get("/")
def home():

    return {"status": "Football AI Chatbot running"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = chatbot.answer(
        message=request.message, selected_player=request.selected_player
    )

    return ChatResponse(answer=answer)
