from pydantic import BaseModel


class ChatRequest(BaseModel):

    message: str

    selected_player: str | None = None
