from enum import Enum


class CreateCrossSectionLinesProjectsProjectIdCrossSectionsLinesFormatPostFormat(str, Enum):
    DXF = "dxf"
    SHP = "shp"

    def __str__(self) -> str:
        return str(self.value)
