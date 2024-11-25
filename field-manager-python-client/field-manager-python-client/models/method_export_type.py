from enum import Enum


class MethodExportType(str, Enum):
    SND = "SND"

    def __str__(self) -> str:
        return str(self.value)
