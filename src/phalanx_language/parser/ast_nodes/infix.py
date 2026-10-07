from dataclasses import dataclass

from phalanx_language.lexer.tokens import Token
from phalanx_language.parser.ast_nodes.base import ExpressionNode


@dataclass
class BinaryOpNode(ExpressionNode):
    left: ExpressionNode
    operator: Token  # Or TokenType
    right: ExpressionNode
