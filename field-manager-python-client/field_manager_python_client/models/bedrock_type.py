from enum import Enum


class BedrockType(str, Enum):
    BEDROCK = "BEDROCK"
    POSSIBLY_BEDROCK = "POSSIBLY_BEDROCK"
    ROCK_LAYER = "ROCK_LAYER"

    def __str__(self) -> str:
        return str(self.value)
