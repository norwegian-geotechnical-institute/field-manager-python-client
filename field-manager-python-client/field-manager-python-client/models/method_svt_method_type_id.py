from enum import IntEnum


class MethodSVTMethodTypeId(IntEnum):
    VALUE_10 = 10

    def __str__(self) -> str:
        return str(self.value)
