class IntentEngine:

    soccer_words = [
        "soccer",
        "football",
        "player",
        "team",
        "touch",
        "pass",
        "movement",
        "position",
        "speed",
        "distance",
        "mistake",
        "decision",
        "performance",
        "run",
        "analysis",
    ]

    compliment_words = [
        "perfect",
        "great",
        "excellent",
        "awesome",
        "amazing",
        "good job",
    ]

    thanks_words = ["thank", "thanks", "ok", "okay", "understand", "got it"]

    @staticmethod
    def is_soccer(message):

        text = message.lower()

        return any(word in text for word in IntentEngine.soccer_words)

    @staticmethod
    def is_compliment(message):

        text = message.lower()

        return any(word in text for word in IntentEngine.compliment_words)

    @staticmethod
    def is_thanks(message):

        text = message.lower()

        return any(word in text for word in IntentEngine.thanks_words)
