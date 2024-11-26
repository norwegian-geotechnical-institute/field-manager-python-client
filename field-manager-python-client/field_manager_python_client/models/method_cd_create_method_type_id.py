from enum import IntEnum


class MethodCDCreateMethodTypeId(IntEnum):
    VALUE_12 = 12

    def __str__(self) -> str:
        return str(self.value)
