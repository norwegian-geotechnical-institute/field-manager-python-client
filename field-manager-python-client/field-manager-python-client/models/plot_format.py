from enum import Enum

class PlotFormat(str, Enum):
    DYNAMIC = "dynamic"
    PDF = "pdf"
    PREVIEW = "preview"
    STATIC = "static"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
