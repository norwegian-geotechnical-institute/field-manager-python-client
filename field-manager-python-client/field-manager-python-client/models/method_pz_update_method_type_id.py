from enum import IntEnum


class MethodPZUpdateMethodTypeId(IntEnum):
    VALUE_5 = 5

    def __str__(self) -> str:
        return str(self.value)
