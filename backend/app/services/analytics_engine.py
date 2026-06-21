class AnalyticsEngine:

    def get_metric(self, player, metric):

        counts = player["counts"]

        movement = player["movement_stats"]

        mapping = {
            "touches": counts["touches"],
            "passes": counts["passes"],
            "good_decisions": counts["good_decisions"],
            "bad_decisions": counts["bad_decisions"],
            "good_runs": counts["good_runs"],
            "max_speed": movement["max_speed_ms"],
            "avg_speed": movement["avg_speed_ms"],
            "distance": movement["distance_m"],
        }

        return mapping.get(metric)
