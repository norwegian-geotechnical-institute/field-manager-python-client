from enum import IntEnum


class MethodESAMethodTypeId(IntEnum):
    VALUE_15 = 15

    def __str__(self) -> str:
        return str(self.value)
