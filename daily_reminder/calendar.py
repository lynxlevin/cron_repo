import math
from datetime import datetime


class Calendar(datetime):
    def nth_week(self):
        return math.ceil(self.day / 7)
