from enum import Enum


class RoleEntityEnum(str, Enum):
    ORG = "org"
    PROJ = "proj"

    def __str__(self) -> str:
        return str(self.value)
