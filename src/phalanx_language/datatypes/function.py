from dataclasses import dataclass
from typing import List

from phalanx_language.datatypes.base import Value
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.functions import FunctionParamsNode
from phalanx_language.parser.ast.prefix import NullNode


@dataclass(frozen=True, slots=True)
class Function(Value):
    name: str
    params: List[FunctionParamsNode]
    code_block: List[ExpressionNode]
    closure_env: Enviroment

    def type_name(self) -> str:
        return "function"

    def is_truthy(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"<function:{self.name}>"
