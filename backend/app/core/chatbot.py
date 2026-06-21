from app.services.question_understanding import QuestionUnderstandingEngine

from app.services.analytics_engine import AnalyticsEngine

from app.services.performance_engine import PerformanceEngine

from app.services.openai_service import OpenAIService

from app.services.intent_engine import IntentEngine

from app.services.response_generator import ResponseGenerator

from app.core.constants import COMPLIMENT_RESPONSE, THANK_RESPONSE, REFUSAL_RESPONSE


class SoccerChatbot:

    def __init__(self, data):

        self.data = data

        self.understanding_engine = QuestionUnderstandingEngine()

        self.analytics_engine = AnalyticsEngine()

        self.performance_engine = PerformanceEngine()

        self.openai = OpenAIService()

        self.response_generator = ResponseGenerator()

    def get_player(self, selected_player):

        return self.data.get("player_analytics", {}).get(selected_player)

    def answer(self, message, selected_player=None):

        print(f"[DEBUG] Player: " f"{selected_player}")

        #
        # COMPLIMENT
        #

        if IntentEngine.is_compliment(message):

            return COMPLIMENT_RESPONSE

        #
        # THANKS
        #

        if IntentEngine.is_thanks(message):

            return THANK_RESPONSE

        #
        # PLAYER REQUIRED
        #

        if not selected_player:

            return "Please select a player."

        player = self.get_player(selected_player)

        if not player:

            return "Selected player not found."

        #
        # UNDERSTAND QUESTION
        #

        understanding = self.understanding_engine.understand(message)

        print("[DEBUG]", understanding)

        #
        # FULL REPORT
        #

        if understanding.intent == "full_report":

            counts = player["counts"]

            movement = player["movement_stats"]

            result = self.performance_engine.evaluate(player)

            return f"""
PLAYER REPORT

Performance:
{result['rating']}

Good Decisions:
{result['good_decisions']}

Statistics
----------
Touches:
{counts['touches']}

Passes:
{counts['passes']}

Movements:
{counts['movements']}

Positioning:
{counts['positioning']}

Mistakes:
{counts['mistakes']}

Good Decisions:
{counts['good_decisions']}

Bad Decisions:
{counts['bad_decisions']}

Opportunities Missed:
{counts['opportunities_missed']}

Good Runs:
{counts['good_runs']}

Movement Statistics
-------------------
Distance Covered:
{movement['distance_m']}

Maximum Speed:
{movement['max_speed_ms']}

Average Speed:
{movement['avg_speed_ms']}
"""

        #
        # PERFORMANCE
        #

        if understanding.intent == "performance":

            result = self.performance_engine.evaluate(player)

            return (
                f"Performance: "
                f"{result['rating']}\n\n"
                f"Good Decisions: "
                f"{result['good_decisions']}"
            )

        #
        # DATA QUERY
        #

        if understanding.intent == "data_query":

            value = self.analytics_engine.get_metric(player, understanding.metric)

            if value is None:

                return "Data not available."
            
            return self.response_generator.generate(understanding.metric, value)

        #
        # GPT SOCCER KNOWLEDGE
        #

        if understanding.intent == "soccer_knowledge":

            return self.openai.ask(message)

        return REFUSAL_RESPONSE
