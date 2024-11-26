from enum import Enum


class ScalingMode(str, Enum):
    AUTO = "auto"
    MANUAL = "manual"
    PERCENTILE = "percentile"

    def __str__(self) -> str:
        return str(self.value)
