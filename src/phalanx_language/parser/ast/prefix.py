from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast.base import ExpressionNode, LiteralNode


@dataclass(frozen=True)
class IntegerLiteralNode(LiteralNode):
    """Represents integer literals (e.g., 42)."""

    # Only to tell pyright the return type
    @property
    def value(self) -> int:
        return super().value

    def __repr__(self) -> str:
        return super().__repr__()


@dataclass(frozen=True)
class FloatLiteralNode(LiteralNode):
    """Represents floating point literals (e.g., 3.14)."""

    @property
    def value(self) -> float:
        return super().value

    def __repr__(self) -> str:
        return super().__repr__()
