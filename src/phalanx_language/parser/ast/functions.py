from dataclasses import dataclass
from typing import List

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.prefix import NullNode


@dataclass(frozen=True)
class FunctionParamsNode(ExpressionNode):
    name: Token
    var_type: Token

    def __repr__(self) -> str:
        return f"{self.name}::{self.var_type}"


@dataclass(frozen=True)
class FunctionDeclerationNode(ExpressionNode):
    name: Token
    args: List[FunctionParamsNode]
    return_type: Token
    code_block: List[ExpressionNode]

    def __repr__(self) -> str:
        return f"func {self.name} ({self.args}) {self.code_block}"


@dataclass(frozen=True)
class FunctionCallNode(ExpressionNode):
    name: Token
    args: List[ExpressionNode]

    def __repr__(self) -> str:
        return f"func {self.name} ({self.args})"


@dataclass(frozen=True, slots=True)
class ReturnNode(ExpressionNode):
    expr: ExpressionNode | None

    def __repr__(self) -> str:
        return f"return {self.expr}"
