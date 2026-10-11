from typing import Dict, Optional

from phalanx_language.datatypes.base import Value


class Enviroment:
    def __init__(self) -> None:
        self.values: Dict[str, Value] = {}
        self.parent: Optional[Enviroment] = None

    def define(self, name: str, value: Value) -> None:
        self.values[name] = value

    def assign(self, name: str, value: Value):
        if name in self.values:
            self.values[name] = value
            return

        if self.parent is not None:
            self.parent.assign(name, value)
            return

        raise NameError(f"No variable with the name {name} to assign value to")

    def get(self, name: str):
        if name in self.values:
            return self.values[name]

        if self.parent is not None:
            return self.parent.get(name)

        raise NameError(f"No variable with the name {name}")
