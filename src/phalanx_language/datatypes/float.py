from dataclasses import dataclass

from phalanx_language.datatypes.base import Value
from phalanx_language.datatypes.int import Integer


@dataclass(frozen=True, slots=True)
class Float(Value):
    value: float

    def type_name(self) -> str:
        return "Float"

    def is_truthy(self) -> bool:
        return self.value != 0

    def __str__(self) -> str:
        return f"{self.value}"

    def __add__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(self.value + other.value)

        return NotImplemented

    def __radd__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            # __r*__ have inverted operand. 10/2.0 -> 10 is other and 2.0 is self
            return Float(other.value + self.value)

        return NotImplemented

    def __sub__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(self.value - other.value)

        return NotImplemented

    def __rsub__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(other.value - self.value)

        return NotImplemented

    def __mul__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(self.value * other.value)

        return NotImplemented

    def __rmul__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(other.value * self.value)

        return NotImplemented

    def __truediv__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(self.value / other.value)

        return NotImplemented

    def __rtruediv__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(other.value / self.value)

        return NotImplemented

    def __mod__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            return Float(self.value % other.value)

        return NotImplemented

    def __rmod__(self, other: Value) -> Value:
        if isinstance(other, Float):
            return Float(other.value % self.value)

        return NotImplemented
