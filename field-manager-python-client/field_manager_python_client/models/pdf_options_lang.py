from enum import Enum


class PdfOptionsLang(str, Enum):
    ENG = "eng"
    NOR = "nor"
    SWE = "swe"

    def __str__(self) -> str:
        return str(self.value)
