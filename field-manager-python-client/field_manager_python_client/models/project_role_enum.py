from enum import Enum


class ProjectRoleEnum(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"

    def __str__(self) -> str:
        return str(self.value)
