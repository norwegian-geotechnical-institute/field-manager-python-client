from enum import Enum


class GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat(str, Enum):
    DXF = "dxf"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
