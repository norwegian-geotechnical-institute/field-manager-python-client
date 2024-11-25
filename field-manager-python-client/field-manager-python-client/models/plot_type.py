from enum import Enum


class PlotType(str, Enum):
    ALL = "all"
    CPT = "cpt"
    DP = "dp"
    PZ = "pz"
    RCD = "rcd"
    RP = "rp"
    SRS = "srs"
    SS = "ss"
    SVT = "svt"
    TOT = "tot"
    WST = "wst"

    def __str__(self) -> str:
        return str(self.value)
