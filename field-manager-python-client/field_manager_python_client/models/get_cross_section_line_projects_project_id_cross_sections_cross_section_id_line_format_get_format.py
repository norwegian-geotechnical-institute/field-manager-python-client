from enum import Enum


class GetCrossSectionLineProjectsProjectIdCrossSectionsCrossSectionIdLineFormatGetFormat(str, Enum):
    DXF = "dxf"
    SHP = "shp"

    def __str__(self) -> str:
        return str(self.value)
