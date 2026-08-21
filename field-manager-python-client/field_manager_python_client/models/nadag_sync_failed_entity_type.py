from enum import Enum


class NadagSyncFailedEntityType(str, Enum):
    COMMAND = "COMMAND"
    FILE = "FILE"
    LOCATION = "LOCATION"
    PROJECT = "PROJECT"

    def __str__(self) -> str:
        return str(self.value)
