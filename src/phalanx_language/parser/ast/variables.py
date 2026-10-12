from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode


@dataclass(frozen=True)
class VariableDeclarationNode(ExpressionNode):
    identifier: Token
    var_type: Token
    expr: ExpressionNode

    def __repr__(self) -> str:
        return f"let {self.identifier}::{self.var_type} = {self.expr}"


@dataclass(frozen=True)
class VariableAccessNode(ExpressionNode):
    identifier: Token

    def __repr__(self) -> str:
        return f"var:{self.identifier}"
