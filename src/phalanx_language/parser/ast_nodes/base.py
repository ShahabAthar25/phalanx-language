from abc import ABC


class ASTNode(ABC):
    """Abstract Base Class for all AST nodes."""

    pass


class ExpressionNode(ASTNode, ABC):
    """Base class for AST nodes that evaluate to a value."""

    pass
