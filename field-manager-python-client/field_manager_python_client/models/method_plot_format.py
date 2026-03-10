from enum import Enum


class MethodPlotFormat(str, Enum):
    DXF = "dxf"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
