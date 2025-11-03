from enum import Enum


class MethodPlotFormat(str, Enum):
    DXF = "dxf"

    def __str__(self) -> str:
        return str(self.value)
