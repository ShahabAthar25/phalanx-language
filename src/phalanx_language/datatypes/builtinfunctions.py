from dataclasses import dataclass
from typing import Callable

from phalanx_language.datatypes.base import Value


@dataclass(frozen=True, slots=True)
class BuiltInFunction(Value):
    value: Callable

    def type_name(self) -> str:
        return "function"

    def is_truthy(self) -> bool:
        return True

    def call(self, args):
        return self.value(*args)

    def __str__(self) -> str:
        return "<function builtin=true>"
