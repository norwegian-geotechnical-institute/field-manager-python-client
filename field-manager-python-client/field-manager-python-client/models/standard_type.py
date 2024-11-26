from enum import Enum


class StandardType(str, Enum):
    IOGP = "IOGP"
    NGF = "NGF"
    OW = "OW"
    SGF = "SGF"

    def __str__(self) -> str:
        return str(self.value)
