import unittest
from unittest import mock

from index import DailyReminder
from mod_datetime import ModDatetime


class TestDailyReminder(unittest.TestCase):
    def test_exec__no_arg(self):
        daily_reminder = DailyReminder()
        result = daily_reminder.exec()
        self.assertEqual([], result)

    @mock.patch("slack_messenger.SlackMessenger.send_message")
    @mock.patch("mod_datetime.ModDatetime.today")
    def test_exec__trash_reminder(self, mod_datetime_mock, messenger_mock):
        def get_expected(day):
            suffix = "の日です。"
            if day in [3, 6, 10, 13, 17, 20, 24, 27, 31]:
                return f"燃やすゴミ{suffix}"
            if day in [4, 18]:
                return f"紙布{suffix}"
            if day in [5, 19]:
                return f"缶瓶{suffix}"
            if day in [7, 14, 21, 28]:
                return f"プラスチック{suffix}"
            if day in [11, 25]:
                return f"ペットボトル{suffix}"
            if day in [12, 26]:
                return f"小型不燃{suffix}"
            return None

        for i in range(1, 32):
            with self.subTest(case=f"2025/03/{i}: {get_expected(i)}"):
                mod_datetime_mock.return_value = ModDatetime(2025, 3, i)
                daily_reminder = DailyReminder()
                daily_reminder.exec(trash_schedule=True)

                expected = get_expected(i)
                self.assertEqual([expected], daily_reminder.messages)
                if expected is not None:
                    messenger_mock.assert_called_once_with("url", {"text": expected})
                messenger_mock.reset_mock()


class TestModDatetime(unittest.TestCase):
    def test_nth_week(self):
        cases = [
            {"day": 2, "nth_week": 1},
            {"day": 7, "nth_week": 1},
            {"day": 8, "nth_week": 2},
            {"day": 14, "nth_week": 2},
            {"day": 15, "nth_week": 3},
            {"day": 21, "nth_week": 3},
            {"day": 22, "nth_week": 4},
            {"day": 28, "nth_week": 4},
            {"day": 29, "nth_week": 5},
            {"day": 31, "nth_week": 5},
        ]
        for case in cases:
            day = case["day"]
            nth_week = case["nth_week"]

            with self.subTest(case=f"2024/1/{day}"):
                mod_date = ModDatetime(year=2024, month=1, day=day)
                result = mod_date.nth_week()
                self.assertEqual(nth_week, result)


if __name__ == "__main__":
    """
    python daily_reminder/test_daily_reminder.py
    """
    unittest.main()
