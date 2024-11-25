from enum import IntEnum


class MethodPZDataMethodTypeId(IntEnum):
    VALUE_5 = 5

    def __str__(self) -> str:
        return str(self.value)
