from enum import IntEnum


class MethodSRSDataMethodTypeId(IntEnum):
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
