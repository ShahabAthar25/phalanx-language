from typing import TYPE_CHECKING, Dict, Optional, Type

from phalanx_language.datatypes.base import Value
from phalanx_language.datatypes.bool import Boolean
from phalanx_language.datatypes.float import Float
from phalanx_language.datatypes.int import Integer
from phalanx_language.datatypes.null import Null
from phalanx_language.datatypes.vector import Vector
from phalanx_language.lexer.tokens import Token, TokenTypes
from phalanx_language.parser.ast.variables import VariableAccessNode

if TYPE_CHECKING:
    from phalanx_language.datatypes.function import Function

TYPE_REGISTRY: Dict[str, type] = {
    "int": Integer,
    "float": Float,
    "bool": Boolean,
    "null": Null,
    "vector": Vector,
}


class Enviroment:
    def __init__(self, parent=None) -> None:
        self.values: Dict[str, Value] = {}
        self.types: Dict[str, type] = {}

        self.parent: Optional[Enviroment] = parent

    def _check_type(self, name: str, value: Value, var_type: str | Type) -> Type:
        actual_type = type(value)

        if isinstance(var_type, str):
            if var_type not in TYPE_REGISTRY:
                raise TypeError(f"TypeError: Unknown type '{var_type}'")

            expected_type = TYPE_REGISTRY[var_type]

        elif isinstance(var_type, type):
            expected_type = var_type

        else:
            raise TypeError(
                f"Unexpected type encountered while defining variable. '{var_type}'"
            )

        if not isinstance(value, expected_type):
            var_type_err = var_type.value if isinstance(var_type, Token) else var_type
            raise TypeError(
                f"Type mismatch in declaration of '{name}'. "
                f"Expected type '{var_type_err}', but expression evaluated to {actual_type.__name__}."
            )

        return expected_type

    def define(self, name: str, value: Value, var_type: str) -> None:
        if self.get(name) is not None:
            raise NameError("Variable already defined in local or global scope.")

        stored_type = self._check_type(name, value, var_type)

        self.values[name] = value
        self.types[name] = stored_type

    def define_function(self, name: str, func_value: Function) -> None:
        if self.get(name) is not None:
            raise NameError(f"'{name}' is already defined.")

        self.values[name] = func_value
        self.types[name] = type(func_value)

    def assign(self, name: str, value: Value):
        if name in self.values:
            var_type = self.types[name]
            self._check_type(name, value, var_type)

            self.values[name] = value
            return

        if self.parent is not None:
            self.parent.assign(name, value)
            return

        raise NameError(f"No variable with the name {name} to assign value to")

    def get(self, name: str) -> Value | None:
        if name in self.values:
            return self.values[name]

        if self.parent is not None:
            return self.parent.get(name)

        return None

    def retrieve(self, name: str) -> Value:
        value = self.get(name)

        if value is None:
            raise NameError(f"No variable with the name {name}")

        return value
