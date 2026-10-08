from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode


@dataclass(frozen=True)
class BinaryOpNode(ExpressionNode):
    left: ExpressionNode
    operator: Token
    right: ExpressionNode

    def __repr__(self) -> str:
        return f"({self.left} {self.operator} {self.right})"
