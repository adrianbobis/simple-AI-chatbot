from openai import OpenAI

from app.core.config import OPENAI_API_KEY, OPENAI_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


class OpenAIService:

    def ask(self, message):

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a soccer expert.
                    Answer football questions accurately.
                    Do not invent match statistics.
                    """,
                },
                {"role": "user", "content": message},
            ],
        )

        return response.choices[0].message.content
