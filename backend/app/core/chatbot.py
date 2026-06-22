
from app.services.question_understanding import QuestionUnderstandingEngine
from app.services.analytics_engine import AnalyticsEngine
from app.services.performance_engine import PerformanceEngine
from app.services.openai_service import OpenAIService
from app.services.response_generator import ResponseGenerator

class SoccerChatbot:

    def __init__(self,data):
        self.data=data
        self.understanding_engine=QuestionUnderstandingEngine()
        self.analytics_engine=AnalyticsEngine()
        self.performance_engine=PerformanceEngine()
        self.openai=OpenAIService()
        self.response_generator=ResponseGenerator()

    def get_player(self, selected_player):
        return self.data.get("player_analytics",{}).get(selected_player)

    def answer(self,message,selected_player=None):
        result=self.understanding_engine.understand(message)

        if result.intent=="social":
            return "Hello! Ask me about the selected player or football."

        if result.intent=="soccer_knowledge":
            return self.openai.ask(message)

        if not selected_player:
            return "Please select a player first."

        player=self.get_player(selected_player)
        if not player:
            return "Selected player not found."

        if result.intent=="performance":
            perf=self.performance_engine.evaluate(player)
            return (
                f"Overall performance: {perf['rating']}. "
                f"The player recorded {perf['good_decisions']} good decisions, "
                f"{perf['good_runs']} good runs and "
                f"{perf['positioning']} positioning events."
            )

        if result.intent=="data_query":
            value=self.analytics_engine.get_metric(player,result.metric)
            if value is None:
                return "I couldn't find information about that aspect of the selected player in the available analysis data."
            return self.response_generator.generate(result.metric,value)

        if result.intent=="full_report":
            c=player["counts"]
            m=player["movement_stats"]
            return f"""Player Report

Touches: {c['touches']}
Passes: {c['passes']}
Movements: {c['movements']}
Positioning: {c['positioning']}
Good Decisions: {c['good_decisions']}
Bad Decisions: {c['bad_decisions']}
Good Runs: {c['good_runs']}

Distance Covered: {m['distance_m']} m
Maximum Speed: {m['max_speed_ms']} m/s
Average Speed: {m['avg_speed_ms']} m/s
"""

        return "Unable to process request."
