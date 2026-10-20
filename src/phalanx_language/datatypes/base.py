# phalanx_language/interpreter/values.py

from abc import ABC, abstractmethod
from typing import Any


class Value(ABC):
    """Abstract Base Class for all Phalanx runtime values."""

    # Underlying Python primitive (int, float, str, bool, etc.).
    value: Any

    @abstractmethod
    def is_truthy(self) -> bool:
        """Determines truthiness in if/while conditions."""
        pass

    def negate(self) -> bool:
        return not self.is_truthy()

    @abstractmethod
    def type_name(self) -> str:
        """Human-readable type string for runtime errors (e.g. 'integer', 'string')."""
        pass

    def get_attribute(self, attr: str):
        raise TypeError(
            f"Property accessor for attribute {attr} not supported on this data type {self.type_name}"
        )

    @abstractmethod
    def __str__(self) -> str:
        """Printable representation."""
        pass

    def __eq__(self, other: object) -> bool:
        """Default structural equality check."""
        if isinstance(other, Value):
            return type(self) is type(other) and self.value == other.value

        return False

    # Arithmatic Oprations

    def __add__(self, other: "Value") -> "Value":
        raise NotImplementedError(
            f"Operator '+' not supported for {type(self).__name__}"
        )

    def __sub__(self, other: "Value") -> "Value":
        raise NotImplementedError(
            f"Operator '-' not supported for {type(self).__name__}"
        )

    def __mul__(self, other: "Value") -> "Value":
        raise NotImplementedError(
            f"Operator '*' not supported for {type(self).__name__}"
        )

    def __truediv__(self, other: "Value") -> "Value":
        raise NotImplementedError(
            f"Operator '/' not supported for {type(self).__name__}"
        )

    def __mod__(self, other: "Value") -> "Value":
        raise NotImplementedError(
            f"Operator '%' not supported for {type(self).__name__}"
        )
