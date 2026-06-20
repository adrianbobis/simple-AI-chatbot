from app.services.intent_engine import IntentEngine

from app.services.query_engine import QueryEngine

from app.services.openai_service import OpenAIService

from app.core.constants import *


class SoccerChatbot:

    def __init__(self, data):

        self.query = QueryEngine(data)

        self.openai = OpenAIService()

    def answer(self, message, selected_player=None):

        # Soccer path

        if IntentEngine.is_soccer(message):

            data_answer = self.query.query(message, selected_player)

            if data_answer:

                return data_answer

            return self.openai.ask(message)

        # Non soccer path

        if IntentEngine.is_compliment(message):

            return COMPLIMENT_RESPONSE

        if IntentEngine.is_thanks(message):

            return THANK_RESPONSE

        return REFUSAL_RESPONSE
