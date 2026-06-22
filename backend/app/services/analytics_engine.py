
class AnalyticsEngine:
    def get_metric(self, player, metric):
        counts = player["counts"]
        movement = player["movement_stats"]

        mapping = {
            "touches": counts["touches"],
            "passes": counts["passes"],
            "positioning": counts["positioning"],
            "movements": movement,
            "good_decisions": player["good_decisions"],
            "bad_decisions": player["bad_decisions"],
            "good_runs": player["good_runs"],
            "mistakes": player["mistakes"],
            "max_speed": movement["max_speed_ms"],
            "avg_speed": movement["avg_speed_ms"],
            "distance": movement["distance_m"],
        }
        return mapping.get(metric)
