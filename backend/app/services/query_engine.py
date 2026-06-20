import re

from app.services.performance_engine import PerformanceEngine


class QueryEngine:

    def __init__(self, data):

        self.data = data

        self.performance_engine = PerformanceEngine()

    def get_player(self, player_key):

        return self.data["player_analytics"].get(player_key)

    def resolve_player(self, message, selected_player):

        match = re.search(r"player\s*(\d+).*team\s*(\d+)", message.lower())

        if match:

            team = match.group(2)

            player = match.group(1)

            return f"team_{team}_player_{player}"

        return selected_player

    def query(self, message, selected_player):

        player_key = self.resolve_player(message, selected_player)

        if not player_key:

            return None

        player = self.get_player(player_key)

        if not player:

            return None

        text = message.lower()

        counts = player["counts"]

        # Direct statistics

        if "touch" in text:

            return str(counts["touches"])

        if "pass" in text:

            return str(counts["passes"])

        if "mistake" in text:

            return str(counts["mistakes"])

        if "good decision" in text:

            return str(counts["good_decisions"])

        if "bad decision" in text:

            return str(counts["bad_decisions"])

        if "good run" in text:

            return str(counts["good_runs"])

        # Performance question

        if "performance" in text or "how was" in text or "analyze" in text:

            result = self.performance_engine.evaluate(player)

            return (
                f"Performance: "
                f"{result['rating']}.\n"
                f"Good decisions: "
                f"{result['good_decisions']}."
            )

        return None
