from enum import Enum


class DPType(str, Enum):
    DPH = "DPH"
    DPL = "DPL"
    DPM = "DPM"
    DPSHA = "DPSHA"
    DPSHB = "DPSHB"

    def __str__(self) -> str:
        return str(self.value)
