import unittest
from calendar import Calendar
from unittest import mock

from index import DailyReminder


class TestDailyReminder(unittest.TestCase):
    def test_exec__no_arg(self):
        daily_reminder = DailyReminder()
        result = daily_reminder.exec()
        self.assertEqual("no_exc", result)

    def test_exec__trash_reminder(self):
        expected = {
            3: "燃やすゴミ",
            4: "紙布",
            5: "缶瓶",
            6: "燃やすゴミ",
            7: "プラスチック",
            10: "燃やすゴミ",
            11: "ペットボトル",
            12: "小型不燃",
            13: "燃やすゴミ",
            14: "プラスチック",
            17: "燃やすゴミ",
            18: "紙布",
            19: "缶瓶",
            20: "燃やすゴミ",
            21: "プラスチック",
            24: "燃やすゴミ",
            25: "ペットボトル",
            26: "小型不燃",
            27: "燃やすゴミ",
            28: "プラスチック",
            31: "燃やすゴミ",
        }

        for i in range(1, 32):
            with self.subTest(case=f"2025/03/{i}: {expected.get(i)}"):
                with mock.patch(
                    "calendar.Calendar.today", return_value=Calendar(2025, 3, i)
                ):
                    daily_reminder = DailyReminder()
                    result = daily_reminder.exec(trash_schedule=True)
                    self.assertEqual([expected.get(i)], result)


class TestCalendar(unittest.TestCase):
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
                calendar = Calendar(year=2024, month=1, day=day)
                result = calendar.nth_week()
                self.assertEqual(nth_week, result)


if __name__ == "__main__":
    """
    python daily_reminder/test_daily_reminder.py
    """
    unittest.main()
