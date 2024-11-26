from enum import Enum


class FileType(str, Enum):
    DATA = "DATA"
    GENERAL = "GENERAL"
    IMAGE = "IMAGE"
    LAYER = "LAYER"

    def __str__(self) -> str:
        return str(self.value)
