from enum import Enum


class PiezometerType(str, Enum):
    ELECTRIC = "ELECTRIC"
    HYDRAULIC = "HYDRAULIC"
    STANDPIPE = "STANDPIPE"

    def __str__(self) -> str:
        return str(self.value)
