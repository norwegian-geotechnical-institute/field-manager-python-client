from enum import Enum

class DPType(str, Enum):
    DPH = "DPH"
    DPL = "DPL"
    DPM = "DPM"
    DPSH_A = "DPSH-A"
    DPSH_B = "DPSH-B"

    def __str__(self) -> str:
        return str(self.value)
