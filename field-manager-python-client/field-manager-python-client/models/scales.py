from enum import Enum


class Scales(str, Enum):
    AUTO_SCALING = "Auto scaling"
    FIT_SCALING = "Fit scaling"
    VALUE_10 = "1/250"
    VALUE_11 = "1/300"
    VALUE_12 = "1/350"
    VALUE_13 = "1/400"
    VALUE_14 = "1/450"
    VALUE_15 = "1/500"
    VALUE_16 = "1/600"
    VALUE_17 = "1/750"
    VALUE_18 = "1/800"
    VALUE_19 = "1/1000"
    VALUE_2 = "1/25"
    VALUE_3 = "1/50"
    VALUE_4 = "1/75"
    VALUE_5 = "1/100"
    VALUE_6 = "1/125"
    VALUE_7 = "1/150"
    VALUE_8 = "1/175"
    VALUE_9 = "1/200"

    def __str__(self) -> str:
        return str(self.value)
