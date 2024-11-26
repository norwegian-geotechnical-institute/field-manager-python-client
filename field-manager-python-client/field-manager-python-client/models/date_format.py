from enum import Enum


class DateFormat(str, Enum):
    ISO = "ISO"
    NOR = "NOR"

    def __str__(self) -> str:
        return str(self.value)
