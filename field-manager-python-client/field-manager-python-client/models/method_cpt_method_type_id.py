from enum import IntEnum

class MethodCPTMethodTypeId(IntEnum):
    VALUE_1 = 1

    def __str__(self) -> str:
        return str(self.value)
