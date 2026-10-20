from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode


@dataclass(frozen=True, slots=True)
class DotNode(ExpressionNode):
    left: ExpressionNode
    attr: Token

    def __repr__(self) -> str:
        return f"{self.left}.{self.attr}"
