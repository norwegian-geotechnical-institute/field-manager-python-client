from enum import Enum


class TransformationType(str, Enum):
    ABSOLUTE = "ABSOLUTE"
    NONE = "NONE"
    POLYNOMIAL = "POLYNOMIAL"

    def __str__(self) -> str:
        return str(self.value)
