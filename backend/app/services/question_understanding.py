
from dataclasses import dataclass

@dataclass
class UnderstandingResult:
    intent:str
    metric:str|None=None

class QuestionUnderstandingEngine:
    def understand(self,message:str):
        t=(message or "").lower().strip()

        if t in ["hi","hello","hey","good morning","good evening","bye","goodbye"]:
            return UnderstandingResult("social")

        if any(x in t for x in ["all data","show all","everything","full report","player statistics"]):
            return UnderstandingResult("full_report")

        if any(x in t for x in ["what did this player do well","how did he perform","how was his performance","how was he"]):
            return UnderstandingResult("performance")

        metric_map={
            "touches":["touch","touches"],
            "passes":["pass","passes"],
            "positioning":["positioning"],
            "movements":["movement","movements"],
            "good_decisions":["good decision"],
            "bad_decisions":["bad decision"],
            "mistakes":["mistake","mistakes"],
            "good_runs":["good run"],
            "max_speed":["max speed","maximum speed","top speed"],
            "avg_speed":["average speed"],
            "distance":["distance"]
        }

        for metric, phrases in metric_map.items():
            if any(p in t for p in phrases):
                return UnderstandingResult("data_query", metric)

        return UnderstandingResult("soccer_knowledge")
