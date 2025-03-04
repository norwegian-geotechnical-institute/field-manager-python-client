from enum import Enum


class SoundingClass(str, Enum):
    JB1 = "JB1"
    JB2 = "JB2"
    JB3 = "JB3"
    JBTOT = "JBTOT"

    def __str__(self) -> str:
        return str(self.value)
