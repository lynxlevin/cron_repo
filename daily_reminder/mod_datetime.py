import math
from datetime import datetime


class ModDatetime(datetime):
    def nth_week(self):
        return math.ceil(self.day / 7)
