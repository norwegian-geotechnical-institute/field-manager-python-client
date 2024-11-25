from enum import Enum


class ReadingType(str, Enum):
    POST_INSTALLATION = "POST_INSTALLATION"
    PRE_INSTALLATION = "PRE_INSTALLATION"
    REGULAR = "REGULAR"

    def __str__(self) -> str:
        return str(self.value)
