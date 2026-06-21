from dataclasses import dataclass


@dataclass
class UnderstandingResult:
    intent: str
    metric: str | None = None


class QuestionUnderstandingEngine:

    def understand(self, message: str) -> UnderstandingResult:

        text = message.lower().strip()

        #
        # FULL REPORT
        #

        full_report_patterns = [
            "all data",
            "show all",
            "show everything",
            "everything",
            "full report",
            "complete report",
            "complete analysis",
            "player report",
            "all statistics",
            "all stats",
            "tell me everything",
            "show me everything",
            "give me all data",
            "analyze player",
            "analyze him",
            "analyze her",
        ]

        if any(p in text for p in full_report_patterns):
            return UnderstandingResult(intent="full_report")

        #
        # PERFORMANCE
        #

        performance_patterns = [
            "performance",
            "how was he",
            "how did he perform",
            "how was his game",
            "evaluate him",
            "evaluate player",
            "rate him",
            "overall performance",
            "how good was he",
        ]

        if any(p in text for p in performance_patterns):
            return UnderstandingResult(intent="performance")

        #
        # TOUCHES
        #

        touch_patterns = [
            "touch",
            "touches",
            "touch data",
            "touch statistics",
            "number of touches",
            "touch count",
        ]

        if any(p in text for p in touch_patterns):
            return UnderstandingResult(intent="data_query", metric="touches")

        #
        # PASSES
        #

        pass_patterns = ["pass", "passes", "passing", "pass data", "pass statistics"]

        if any(p in text for p in pass_patterns):
            return UnderstandingResult(intent="data_query", metric="passes")

        #
        # MAX SPEED
        #

        max_speed_patterns = [
            "max speed",
            "maximum speed",
            "highest speed",
            "top speed",
            "speed max",
            "fastest speed",
            "how fast",
        ]

        if any(p in text for p in max_speed_patterns):
            return UnderstandingResult(intent="data_query", metric="max_speed")

        #
        # AVG SPEED
        #

        avg_speed_patterns = ["average speed", "avg speed", "mean speed"]

        if any(p in text for p in avg_speed_patterns):
            return UnderstandingResult(intent="data_query", metric="avg_speed")

        #
        # DISTANCE
        #

        distance_patterns = [
            "distance",
            "distance covered",
            "how far",
            "meters covered",
        ]

        if any(p in text for p in distance_patterns):
            return UnderstandingResult(intent="data_query", metric="distance")

        #
        # GOOD DECISIONS
        #

        if "good decision" in text or "good decisions" in text:
            return UnderstandingResult(intent="data_query", metric="good_decisions")

        #
        # BAD DECISIONS
        #

        if "bad decision" in text or "bad decisions" in text:
            return UnderstandingResult(intent="data_query", metric="bad_decisions")

        #
        # GOOD RUNS
        #

        if "good run" in text or "good runs" in text:
            return UnderstandingResult(intent="data_query", metric="good_runs")

        #
        # SOCCER KNOWLEDGE
        #

        return UnderstandingResult(intent="soccer_knowledge")
