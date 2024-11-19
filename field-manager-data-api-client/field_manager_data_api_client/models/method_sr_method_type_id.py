from enum import IntEnum


class MethodSRMethodTypeId(IntEnum):
    VALUE_20 = 20

    def __str__(self) -> str:
        return str(self.value)
