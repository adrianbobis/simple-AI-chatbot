from app.services.intent_engine import IntentEngine
from app.services.query_engine import QueryEngine
from app.services.openai_service import OpenAIService

from app.core.constants import COMPLIMENT_RESPONSE, THANK_RESPONSE, REFUSAL_RESPONSE


class SoccerChatbot:

    def __init__(self, data):

        self.query_engine = QueryEngine(data)

        self.openai = OpenAIService()

    def answer(self, message, selected_player=None):

        print(f"[DEBUG] Selected Player: {selected_player}")

        # Compliment
        if IntentEngine.is_compliment(message):

            return COMPLIMENT_RESPONSE

        # Thanks
        if IntentEngine.is_thanks(message):

            return THANK_RESPONSE

        # IMPORTANT:
        # If player selected, assume soccer context
        soccer_context = selected_player is not None or IntentEngine.is_soccer(message)

        if not soccer_context:

            return REFUSAL_RESPONSE

        # Try JSON first
        result = self.query_engine.query(message, selected_player)

        if result:

            return result

        # Fallback to GPT soccer knowledge
        return self.openai.ask(message)
