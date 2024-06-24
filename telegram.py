import logging
import config
import requests


def send_telegram_message(message: str):
    token = config.TELEGRAM_BOT_TOKEN
    chat_id = config.TELEGRAM_CHAT_ID
    topic_id = config.TELEGRAM_CHAT_TOPIC_ID
    request_url = f"https://api.telegram.org/bot{token}/sendMessage"
    request_url += f"?chat_id={chat_id}&message_thread_id={topic_id}&text={message}"
    
    response = requests.get(request_url)
    respose_object = response.json()
    ok = respose_object.get("ok", False)
    if not ok:
        logging.error(f'Error sending telegram message: {respose_object}')


if __name__ == "__main__":
    send_telegram_message("Hello, World!")

