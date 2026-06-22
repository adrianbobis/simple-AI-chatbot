
class PerformanceEngine:

    def evaluate(self, player_data):
        counts=player_data["counts"]
        score=0

        score += counts.get("good_decisions",0)*3
        score += counts.get("good_runs",0)*2
        score += counts.get("positioning",0)
        score -= counts.get("bad_decisions",0)*2
        score -= counts.get("mistakes",0)*3

        if score >= 10:
            rating="Excellent"
        elif score >= 5:
            rating="Good"
        elif score >= 1:
            rating="Average"
        else:
            rating="Limited evidence"

        return {
            "rating": rating,
            "score": score,
            "good_decisions": counts.get("good_decisions",0),
            "good_runs": counts.get("good_runs",0),
            "positioning": counts.get("positioning",0),
        }
