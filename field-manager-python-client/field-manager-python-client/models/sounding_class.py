from enum import Enum

class SoundingClass(str, Enum):
    JB_1 = "Jb-1"
    JB_2 = "Jb-2"
    JB_3 = "Jb-3"
    JB_TOT = "Jb-tot"

    def __str__(self) -> str:
        return str(self.value)
