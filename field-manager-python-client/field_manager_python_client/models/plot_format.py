from enum import Enum


class PlotFormat(str, Enum):
    PDF = "pdf"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
