from enum import IntEnum


class MethodRCDUpdateMethodTypeId(IntEnum):
    VALUE_8 = 8

    def __str__(self) -> str:
        return str(self.value)
