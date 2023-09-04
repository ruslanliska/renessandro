import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_EMAIL = os.getenv("DISCORD_EMAIL")
DISCORD_PASSWORD = os.getenv("DISCORD_PASSWORD")
OPENAI_KEY = os.getenv("OPENAI_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
