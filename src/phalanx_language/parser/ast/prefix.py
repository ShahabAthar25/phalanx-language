from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode, LiteralNode


@dataclass(frozen=True)
class IntegerLiteralNode(LiteralNode):
    """Represents integer literals (e.g., 42)."""

    def __repr__(self) -> str:
        return super().__repr__()


@dataclass(frozen=True)
class FloatLiteralNode(LiteralNode):
    """Represents floating point literals (e.g., 3.14)."""

    def __repr__(self) -> str:
        return super().__repr__()
