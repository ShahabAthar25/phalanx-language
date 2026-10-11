from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode


@dataclass(frozen=True)
class VariableDeclarationNode:
    identifier: Token
    type: Token
    expr: ExpressionNode

    def __repr__(self) -> str:
        return f"let {self.identifier}::{self.type} = {self.expr}"
