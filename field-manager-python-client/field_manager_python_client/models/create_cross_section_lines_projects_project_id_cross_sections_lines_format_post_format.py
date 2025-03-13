from enum import Enum


class CreateCrossSectionLinesProjectsProjectIdCrossSectionsLinesFormatPostFormat(str, Enum):
    DXF = "dxf"
    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
