from enum import IntEnum


class MethodSAMethodTypeId(IntEnum):
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
