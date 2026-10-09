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

    @abstractmethod
    def type_name(self) -> str:
        """Human-readable type string for runtime errors (e.g. 'integer', 'string')."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Printable representation."""
        pass

    def __eq__(self, other: object) -> bool:
        """Default structural equality check."""
        if isinstance(other, Value):
            return type(self) is type(other) and self.value == other.value

        return False
