from enum import IntEnum


class MethodSRCreateMethodTypeId(IntEnum):
    VALUE_20 = 20

    def __str__(self) -> str:
        return str(self.value)
