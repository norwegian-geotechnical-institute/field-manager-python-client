from enum import Enum


class LocationType(str, Enum):
    OFFSHORE = "offshore"
    ONSHORE = "onshore"

    def __str__(self) -> str:
        return str(self.value)
