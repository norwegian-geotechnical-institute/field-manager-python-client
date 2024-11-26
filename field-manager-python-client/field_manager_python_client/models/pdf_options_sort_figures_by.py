from enum import Enum


class PdfOptionsSortFiguresBy(str, Enum):
    LOCATION = "location"
    METHOD = "method"

    def __str__(self) -> str:
        return str(self.value)
