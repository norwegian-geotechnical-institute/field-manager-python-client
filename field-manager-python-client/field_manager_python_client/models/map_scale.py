from enum import Enum


class MapScale(str, Enum):
    S_1_100 = "S_1_100"
    S_1_1000 = "S_1_1000"
    S_1_10000 = "S_1_10000"
    S_1_2000 = "S_1_2000"
    S_1_50 = "S_1_50"
    S_1_500 = "S_1_500"
    S_1_5000 = "S_1_5000"

    def __str__(self) -> str:
        return str(self.value)
