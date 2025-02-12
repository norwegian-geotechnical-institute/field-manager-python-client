from enum import Enum


class PdfOptionsDateFormat(str, Enum):
    DD_MM_YYYY = "DD.MM.YYYY"
    YYYY_MM_DD = "YYYY-MM-DD"

    def __str__(self) -> str:
        return str(self.value)
