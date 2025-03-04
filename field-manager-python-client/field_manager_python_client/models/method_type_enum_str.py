from enum import Enum


class MethodTypeEnumStr(str, Enum):
    AD = "ad"
    CD = "cd"
    CPT = "cpt"
    DP = "dp"
    DT = "dt"
    ESA = "esa"
    INC = "inc"
    IW = "iw"
    OTHER = "other"
    PT = "pt"
    PZ = "pz"
    RCD = "rcd"
    RO = "ro"
    RP = "rp"
    RS = "rs"
    RWS = "rws"
    SA = "sa"
    SLB = "slb"
    SPT = "spt"
    SR = "sr"
    SRS = "srs"
    SS = "ss"
    STI = "sti"
    SVT = "svt"
    TOT = "tot"
    TP = "tp"
    TR = "tr"
    WST = "wst"

    def __str__(self) -> str:
        return str(self.value)
