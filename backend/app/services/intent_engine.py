class IntentEngine:

    SOCCER_WORDS = [
        "soccer",
        "football",
        "player",
        "team",
        "touch",
        "touches",
        "pass",
        "passes",
        "movement",
        "positioning",
        "mistake",
        "mistakes",
        "decision",
        "decisions",
        "speed",
        "distance",
        "run",
        "runs",
        "performance",
        "analysis",
        "goal",
        "assist",
    ]

    COMPLIMENT_WORDS = [
        "perfect",
        "great",
        "excellent",
        "awesome",
        "amazing",
        "fantastic",
        "brilliant",
    ]

    THANK_WORDS = ["thank you", "thanks", "okay", "ok", "understood", "got it"]

    @classmethod
    def is_soccer(cls, message):

        text = message.lower()

        return any(word in text for word in cls.SOCCER_WORDS)

    @classmethod
    def is_compliment(cls, message):

        text = message.lower()

        return any(word in text for word in cls.COMPLIMENT_WORDS)

    @classmethod
    def is_thanks(cls, message):

        text = message.lower().strip()

        return any(word in text for word in cls.THANK_WORDS)
