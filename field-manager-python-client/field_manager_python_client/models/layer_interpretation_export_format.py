from enum import Enum


class LayerInterpretationExportFormat(str, Enum):
    CSV_SINGLE = "csv_single"
    CSV_SPLIT = "csv_split"
    JSON = "json"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
