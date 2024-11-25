from enum import IntEnum

class MethodRCDDataUpdateMethodTypeId(IntEnum):
    VALUE_8 = 8

    def __str__(self) -> str:
        return str(self.value)
