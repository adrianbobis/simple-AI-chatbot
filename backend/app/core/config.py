import os

from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")


DATA_PATH = os.getenv("DATA_PATH", "output/data.json")
