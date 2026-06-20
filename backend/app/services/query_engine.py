import re

from app.services.performance_engine import PerformanceEngine


class QueryEngine:

    def __init__(self, data):

        self.data = data

        self.performance_engine = PerformanceEngine()

    def get_player(self, player_key):

        return self.data.get("player_analytics", {}).get(player_key)

    def resolve_player(self, message, selected_player):

        if selected_player:

            return selected_player

        match = re.search(r"player\s*(\d+).*team\s*(\d+)", message.lower())

        if match:

            player_number = match.group(1)

            team_number = match.group(2)

            return f"team_{team_number}_player_{player_number}"

        return None

    def build_full_report(self, player):

        counts = player["counts"]

        movement = player["movement_stats"]

        performance = self.performance_engine.evaluate(player)

        return f"""
PLAYER REPORT

Performance:
{performance['rating']}

Good Decisions:
{performance['good_decisions']}

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

Movement Stats
--------------
Distance Covered:
{movement['distance_m']}

Maximum Speed:
{movement['max_speed_ms']}

Average Speed:
{movement['avg_speed_ms']}
"""

    def query(self, message, selected_player):

        player_key = self.resolve_player(message, selected_player)

        if not player_key:

            return None

        player = self.get_player(player_key)

        if not player:

            return "Player data not found."

        text = message.lower()

        counts = player["counts"]

        # FULL REPORT

        if any(
            phrase in text
            for phrase in [
                "all data",
                "show all",
                "everything",
                "full report",
                "player report",
                "complete analysis",
                "all statistics",
                "show statistics",
                "show stats",
                "tell me everything",
            ]
        ):

            return self.build_full_report(player)

        # TOUCHES

        if "touch" in text:

            return str(counts["touches"])

        # PASSES

        if "pass" in text:

            return str(counts["passes"])

        # GOOD DECISIONS

        if "good decision" in text:

            return str(counts["good_decisions"])

        # BAD DECISIONS

        if "bad decision" in text:

            return str(counts["bad_decisions"])

        # GOOD RUNS

        if "good run" in text:

            return str(counts["good_runs"])

        # MISTAKES

        if "mistake" in text:

            return str(counts["mistakes"])

        # PERFORMANCE QUESTIONS

        if any(
            phrase in text
            for phrase in [
                "performance",
                "how was he",
                "how did he perform",
                "analyze player",
                "analyze him",
                "evaluate player",
                "evaluate him",
            ]
        ):

            result = self.performance_engine.evaluate(player)

            return (
                f"Performance: "
                f"{result['rating']}.\n\n"
                f"Good Decisions: "
                f"{result['good_decisions']}"
            )

        return None
