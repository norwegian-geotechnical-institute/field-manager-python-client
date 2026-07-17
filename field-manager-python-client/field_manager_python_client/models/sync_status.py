from enum import Enum


class SyncStatus(str, Enum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
