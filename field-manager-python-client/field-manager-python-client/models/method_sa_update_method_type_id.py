from enum import IntEnum


class MethodSAUpdateMethodTypeId(IntEnum):
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
