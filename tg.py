import telegram_send


def send_message(msg):
    telegram_send.send(messages=[msg])
