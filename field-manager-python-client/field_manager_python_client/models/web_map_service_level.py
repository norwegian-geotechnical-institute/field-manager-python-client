from enum import Enum


class WebMapServiceLevel(str, Enum):
    APP = "APP"
    ORGANIZATION = "ORGANIZATION"
    PROJECT = "PROJECT"

    def __str__(self) -> str:
        return str(self.value)
