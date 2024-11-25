from enum import Enum


class HeightReference(str, Enum):
    LAT_DEPTH = "LAT_DEPTH"
    MSL_HEIGHT = "MSL_HEIGHT"
    NN1954 = "NN1954"
    NN2000 = "NN2000"
    RH2000 = "RH2000"
    TWVD2001 = "TWVD2001"

    def __str__(self) -> str:
        return str(self.value)
