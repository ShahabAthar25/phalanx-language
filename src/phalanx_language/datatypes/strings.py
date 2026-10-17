from dataclasses import dataclass

from phalanx_language.datatypes.base import Value
from phalanx_language.datatypes.int import Integer


@dataclass(frozen=True, slots=True)
class String(Value):
    value: str

    def type_name(self) -> str:
        return "string"

    def is_truthy(self) -> bool:
        return self.value != ""

    def __str__(self) -> str:
        return self.value

    def __add__(self, other: Value) -> Value:
        if isinstance(other, String):
            return String(self.value + other.value)

        raise TypeError("Operation not supported")

    def __mul__(self, other: Value) -> Value:
        if isinstance(other, Integer):
            return String(self.value * other.value)

        raise TypeError("Unsupported operation")
