import requests

BOT_TOKEN = "8423792460:AAFhQjUPe1FGIfMoWTczcYF1WorjePdE0MI"
id = ["1460730539"]
# CHAT_ID = "1460730539"  # your Telegram user ID or group ID


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in id:
        payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed to send Telegram message: {e}")
