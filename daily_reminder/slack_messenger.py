import json

import requests


class SlackMessenger:
    def send_message(self, channel: str, token: str, text: str):
        url = "https://slack.com/api/chat.postMessage"
        message = {
            "channel": channel,
            "text": text,
        }
        header = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        connect_timeout = 5.0
        read_timeout = 30.0

        message = json.dumps(message)

        response = requests.post(
            url, data=message, headers=header, timeout=(connect_timeout, read_timeout)
        )
        response.raise_for_status()
