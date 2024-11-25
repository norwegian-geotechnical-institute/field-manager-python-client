from enum import IntEnum


class ApplicationClassEnum(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_10 = 10
    VALUE_100 = 100

    def __str__(self) -> str:
        return str(self.value)
