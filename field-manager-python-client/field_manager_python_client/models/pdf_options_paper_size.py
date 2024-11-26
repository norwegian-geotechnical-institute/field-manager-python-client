from enum import Enum


class PdfOptionsPaperSize(str, Enum):
    A3 = "A3"
    A4 = "A4"

    def __str__(self) -> str:
        return str(self.value)
