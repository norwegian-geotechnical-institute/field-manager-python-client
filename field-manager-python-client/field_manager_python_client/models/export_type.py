from enum import Enum


class ExportType(str, Enum):
    LOCATIONCSV = "LocationCSV"
    LOCATIONGEOJSON = "LocationGeoJSON"
    LOCATIONKOF = "LocationKOF"
    LOCATIONLAS = "LocationLAS"
    LOCATIONXLS = "LocationXLS"
    METHODFILES = "MethodFiles"
    METHODSND = "MethodSND"
    METHODXLS = "MethodXLS"
    PROJECTFILES = "ProjectFiles"

    def __str__(self) -> str:
        return str(self.value)
