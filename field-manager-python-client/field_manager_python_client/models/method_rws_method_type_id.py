from enum import IntEnum


class MethodRWSMethodTypeId(IntEnum):
    VALUE_7 = 7

    def __str__(self) -> str:
        return str(self.value)
