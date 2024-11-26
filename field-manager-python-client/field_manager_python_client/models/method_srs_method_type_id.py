from enum import IntEnum


class MethodSRSMethodTypeId(IntEnum):
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
