from dataclasses import dataclass

from phalanx_language.datatypes.base import Value


@dataclass(frozen=True, slots=True)
class Integer(Value):
    value: int

    def type_name(self) -> str:
        return "Interger"

    def is_truthy(self) -> bool:
        return self.value != 0

    def __str__(self) -> str:
        return f"{self.value}"

    def __add__(self, other: Value) -> Value:
        if isinstance(other, Integer):
            return Integer(self.value + other.value)

        return NotImplemented

    def __sub__(self, other: Value) -> Value:
        if isinstance(other, Integer):
            return Integer(self.value - other.value)

        return NotImplemented

    def __mul__(self, other: Value) -> Value:
        # Integer * Integer
        if isinstance(other, Integer):
            return Integer(self.value * other.value)

        # Integer * Float is done via __rmul__ in float
        return NotImplemented

    def __truediv__(self, other: Value) -> Value:
        # Division returns float and thus to avoid circular imports
        # div is handled by __rtruediv__ in float datatype
        return NotImplemented

    def __mod__(self, other: Value) -> Value:
        if isinstance(other, Integer):
            return Integer(self.value % other.value)

        # Modulo with floats is allowed and the logic is done via r dunder method
        # in float.py
        return NotImplemented
