from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token


@dataclass
class IntegerLiteralNode(ExpressionNode):
    """Represents integer literals (e.g., 42)."""

    token: Token
    value: int


@dataclass
class FloatLiteralNode(ExpressionNode):
    """Represents floating point literals (e.g., 3.14)."""

    token: Token
    value: float
