class ResponseGenerator:

    @staticmethod
    def generate(metric, value):

        if metric == "touches":

            return f"The selected player " f"recorded {value} touches."

        if metric == "passes":

            return f"The selected player " f"completed {value} passes."

        if metric == "good_decisions":

            return f"The selected player " f"made {value} good decisions."

        if metric == "bad_decisions":

            return f"The selected player " f"made {value} bad decisions."

        if metric == "good_runs":

            return f"The selected player " f"completed {value} good runs."

        if metric == "distance":

            return f"The selected player " f"covered {value} meters."

        if metric == "max_speed":

            return f"The selected player's " f"maximum speed was " f"{value} m/s."

        if metric == "avg_speed":

            return f"The selected player's " f"average speed was " f"{value} m/s."

        return str(value)
