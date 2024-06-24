import os
from dotenv import load_dotenv


load_dotenv('.env')

MARKET_AUTHORIZATION_TOKEN = os.getenv("MARKET_AUTHORIZATION_TOKEN")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_CHAT_TOPIC_ID = os.getenv("TELEGRAM_CHAT_TOPIC_ID")


if __name__ == "__main__":
    print(MARKET_AUTHORIZATION_TOKEN)
    print(TELEGRAM_BOT_TOKEN)

