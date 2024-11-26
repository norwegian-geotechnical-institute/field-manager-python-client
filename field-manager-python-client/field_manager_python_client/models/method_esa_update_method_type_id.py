from enum import IntEnum


class MethodESAUpdateMethodTypeId(IntEnum):
    VALUE_15 = 15

    def __str__(self) -> str:
        return str(self.value)
