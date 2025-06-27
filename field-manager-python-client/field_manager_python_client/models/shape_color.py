from enum import Enum


class ShapeColor(str, Enum):
    COMMON_BLACK = "COMMON_BLACK"
    NEON_BLUE = "NEON_BLUE"
    NEON_GREEN = "NEON_GREEN"
    NEON_PINK = "NEON_PINK"
    NEON_PURPLE = "NEON_PURPLE"
    NEON_RED = "NEON_RED"
    NEON_YELLOW = "NEON_YELLOW"

    def __str__(self) -> str:
        return str(self.value)
