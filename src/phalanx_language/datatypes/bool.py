from dataclasses import dataclass

from phalanx_language.datatypes.base import Value


@dataclass(frozen=True, slots=True)
class Boolean(Value):
    value: bool

    def type_name(self) -> str:
        return "bool"

    def is_truthy(self) -> bool:
        return self.value

    def __str__(self) -> str:
        return "true" if self.value else "false"
