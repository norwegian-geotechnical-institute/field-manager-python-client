from enum import Enum


class Orientation(str, Enum):
    LANDSCAPE = "LANDSCAPE"
    PORTRAIT = "PORTRAIT"

    def __str__(self) -> str:
        return str(self.value)
