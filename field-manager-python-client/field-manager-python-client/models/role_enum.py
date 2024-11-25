from enum import Enum


class RoleEnum(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    REFERENCE = "reference"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
