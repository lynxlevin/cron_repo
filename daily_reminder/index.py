import argparse


class DailyReminder:
    def __init__(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument("--trash-schedule", action="store_true")
        args = parser.parse_args()

        cls.trash_schedule = args.trash_schedule

    def exec(self):
        print("hi")
        print(self.trash_schedule)


if __name__ == "__main__":
    reminder = DailyReminder()
    reminder.exec()
