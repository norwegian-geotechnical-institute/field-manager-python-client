from enum import IntEnum


class MethodSSDataMethodTypeId(IntEnum):
    VALUE_6 = 6

    def __str__(self) -> str:
        return str(self.value)
