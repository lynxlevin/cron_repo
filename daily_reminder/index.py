import argparse
import os
from datetime import timedelta, timezone
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from mod_datetime import ModDatetime
from slack_messenger import SlackMessenger


class DailyReminder:
    def __init__(cls):
        cls.messages = []
        cls.messenger = SlackMessenger()

        dotenv_path = Path(__file__).parent.with_name(".env")
        load_dotenv(dotenv_path)
        cls.channel = os.environ.get("REMINDER_SLACKCHANNEL")
        cls.token = os.environ.get("REMINDER_SLACKTOKEN")

    def exec(self, trash_schedule=False) -> list[Optional[str]]:
        results = []

        if trash_schedule:
            self.messages.append(self._get_trash_schedule())

        for message in self.messages:
            if message is not None:
                self.messenger.send_message(self.channel, self.token, message)

        return results

    def _get_trash_schedule(self) -> Optional[str]:
        suffix = "の日です。"
        JST = timezone(timedelta(hours=+9), "JST")
        today = ModDatetime.now(JST)
        weekday = today.weekday()
        week_number = today.nth_week()

        # if weekday in [0, 3]:
        #     return f"燃やすゴミ{suffix}"
        # elif weekday == 4:
        #     return f"プラスチック{suffix}"
        if weekday == 6:
            if week_number in [1, 3]:
                return f"紙布{suffix}"
        elif weekday == 1:
            if week_number in [1, 3]:
                return f"紙布{suffix}"
            elif week_number in [2, 4]:
                return f"ペットボトル{suffix}"
        elif weekday == 2:
            if week_number in [1, 3]:
                return f"缶瓶{suffix}"
            elif week_number in [2, 4]:
                return f"小型不燃{suffix}"

        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trash-schedule", action="store_true")
    args = parser.parse_args()

    reminder = DailyReminder()
    reminder.exec(trash_schedule=args.trash_schedule)
