from dataclasses import dataclass

from phalanx_language.datatypes.base import Value


@dataclass(frozen=True)
class Null(Value):
    value: None = None

    def type_name(self) -> str:
        return "null"

    def is_truthy(self) -> bool:
        return False

    def negate(self) -> bool:
        return True

    def __str__(self) -> str:
        return "null"
