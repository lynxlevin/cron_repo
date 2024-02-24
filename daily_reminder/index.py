import argparse
from calendar import Calendar


class DailyReminder:
    def exec(self, trash_schedule=False):
        results = []
        if trash_schedule:
            results.append(self._get_trash_schedule())

        if len(results) == 0:
            return "no_exc"
        return results

    def _get_trash_schedule(self):
        today = Calendar.today()

        if today.weekday() in [0, 3]:
            return "燃やすゴミ"
        elif today.weekday() == 4:
            return "プラスチック"
        elif today.weekday() == 1:
            if today.nth_week() in [1, 3]:
                return "紙布"
            elif today.nth_week() in [2, 4]:
                return "ペットボトル"
        elif today.weekday() == 2:
            if today.nth_week() in [1, 3]:
                return "缶瓶"
            elif today.nth_week() in [2, 4]:
                return "小型不燃"

        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trash-schedule", action="store_true")
    args = parser.parse_args()

    reminder = DailyReminder()
    reminder.exec(trash_schedule=args.trash_schedule)
