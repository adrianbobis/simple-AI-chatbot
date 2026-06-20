class PerformanceEngine:

    THRESHOLD = 20

    def evaluate(self, player_data):

        score = player_data["counts"]["good_decisions"]

        if score >= self.THRESHOLD:

            return {"rating": "Good", "good_decisions": score}

        else:

            return {"rating": "Pathetic", "good_decisions": score}
