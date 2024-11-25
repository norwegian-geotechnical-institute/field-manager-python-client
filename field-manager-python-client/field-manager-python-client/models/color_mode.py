from enum import Enum


class ColorMode(str, Enum):
    COLOR = "color"
    GRAYSCALE = "grayscale"

    def __str__(self) -> str:
        return str(self.value)
