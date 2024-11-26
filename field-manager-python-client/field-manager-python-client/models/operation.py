from enum import Enum


class Operation(str, Enum):
    MANUAL = "MANUAL"
    MECHANICAL = "MECHANICAL"

    def __str__(self) -> str:
        return str(self.value)
