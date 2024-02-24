import argparse
from calendar import Calendar
from typing import Optional


class DailyReminder:
    def __init__(cls):
        cls.messages = []

    def exec(self, trash_schedule=False) -> list[Optional[str]]:
        results = []

        if trash_schedule:
            self.messages.append(self._get_trash_schedule())

        return results

    def _get_trash_schedule(self) -> Optional[str]:
        suffix = "の日です。"
        today = Calendar.today()
        weekday = today.weekday()
        week_number = today.nth_week()

        if weekday in [0, 3]:
            return f"燃やすゴミ{suffix}"
        elif weekday == 4:
            return f"プラスチック{suffix}"
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
