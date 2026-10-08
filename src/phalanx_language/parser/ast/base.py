from abc import ABC
from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token


class ASTNode(ABC):
    """Abstract Base Class for all AST nodes."""

    pass


class ExpressionNode(ASTNode, ABC):
    """Base class for AST nodes that evaluate to a value."""

    pass


@dataclass(frozen=True)
class LiteralNode(ExpressionNode, ABC):
    """Base class for all literal nodes (int, float, string, bool)."""

    token: Token

    @property
    def value(self):
        """Single inherited property for all literal nodes."""
        return self.token.value

    def __repr__(self) -> str:
        return f"{self.token}"
