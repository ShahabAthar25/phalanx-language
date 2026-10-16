from dataclasses import dataclass

import polars as pl

from phalanx_language.datatypes.base import Value
from phalanx_language.datatypes.float import Float
from phalanx_language.datatypes.int import Integer
from phalanx_language.interpreter.data_store import DataStore


@dataclass(frozen=True, slots=True)
class Vector(Value):
    value: pl.Series

    def type_name(self) -> str:
        return "vector"

    def is_truthy(self) -> bool:
        return True

    def __str__(self) -> str:
        return str(self.value)

    def __add__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(self.value + other.value)

        return NotImplemented("Unsupported addition between types")

    def __radd__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(other.value + self.value)

        return NotImplemented("Unsupported addition between types")

    def __sub__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(self.value - other.value)

        return NotImplemented("Unsupported addition between types")

    def __rsub__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(other.value - self.value)

        return NotImplemented("Unsupported addition between types")

    def __mul__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(self.value * other.value)

        return NotImplemented("Unsupported addition between types")

    def __rmul__(self, other: Value) -> Value:
        if isinstance(other, (Vector, Integer, Float)):
            return Vector(other.value * self.value)

        return NotImplemented("Unsupported addition between types")

    def __truediv__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            if other.value == 0:
                raise RuntimeError("Division by zero")
            return Vector(self.value / other.value)

        elif isinstance(other, Vector):
            return Vector(self.value / other.value)

        return NotImplemented("Unsupported addition between types")

    def __rtruediv__(self, other: Value) -> Value:
        if isinstance(other, (Integer, Float)):
            if other.value == 0:
                raise RuntimeError("Division by zero")
            return Vector(other.value / self.value)

        elif isinstance(other, Vector):
            return Vector(other.value / self.value)

        return NotImplemented("Unsupported addition between types")
