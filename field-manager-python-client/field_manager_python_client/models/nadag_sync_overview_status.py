from enum import Enum


class NadagSyncOverviewStatus(str, Enum):
    ALL_SYNCED_OK = "ALL_SYNCED_OK"
    NOT_REQUIRED = "NOT_REQUIRED"
    SYNCED_WITH_ERRORS = "SYNCED_WITH_ERRORS"
    SYNC_CANDIDATES_EXIST = "SYNC_CANDIDATES_EXIST"

    def __str__(self) -> str:
        return str(self.value)
