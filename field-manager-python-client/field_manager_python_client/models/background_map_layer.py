from enum import Enum


class BackgroundMapLayer(str, Enum):
    BACKGROUND_NORWAY = "BACKGROUND_NORWAY"
    GEBCO_WORLD = "GEBCO_WORLD"
    NORWAY_TOPOGRAPHIC = "NORWAY_TOPOGRAPHIC"
    NORWAY_TOPOGRAPHIC_GRAYSCALE = "NORWAY_TOPOGRAPHIC_GRAYSCALE"
    SATELLITE_NORWAY = "SATELLITE_NORWAY"
    STREET_MAP_WORLD = "STREET_MAP_WORLD"

    def __str__(self) -> str:
        return str(self.value)
