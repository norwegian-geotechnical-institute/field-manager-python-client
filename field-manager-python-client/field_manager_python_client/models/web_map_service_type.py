from enum import Enum


class WebMapServiceType(str, Enum):
    WFS = "WFS"
    WMS = "WMS"
    WMTS = "WMTS"

    def __str__(self) -> str:
        return str(self.value)
