from enum import Enum


class Language(str, Enum):
    ENG = "eng"
    FIN = "fin"
    NOR = "nor"
    SWE = "swe"

    def __str__(self) -> str:
        return str(self.value)
