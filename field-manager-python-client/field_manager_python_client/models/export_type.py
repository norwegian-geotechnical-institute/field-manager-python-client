from enum import Enum


class ExportType(str, Enum):
    LOCATIONCSV = "LocationCSV"
    LOCATIONGEOJSON = "LocationGeoJSON"
    LOCATIONKOF = "LocationKOF"
    LOCATIONXLS = "LocationXLS"
    METHODFILES = "MethodFiles"
    METHODSND = "MethodSND"
    METHODXLS = "MethodXLS"
    PROJECTFILES = "ProjectFiles"

    def __str__(self) -> str:
        return str(self.value)
