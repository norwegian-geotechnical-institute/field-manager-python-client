from enum import IntEnum


class MethodCDUpdateMethodTypeId(IntEnum):
    VALUE_12 = 12

    def __str__(self) -> str:
        return str(self.value)
