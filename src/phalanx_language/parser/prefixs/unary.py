from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.prefix import UnaryNode
from phalanx_language.parser.binding_power import BindingPower

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_unary(parser: Parser) -> ExpressionNode:
    operator = parser.current_tok

    parser.advance()

    expr = parser.parse_expr(
        parser.binding_powers.get(operator.type, BindingPower.ASSIGN)
    )

    return UnaryNode(operator, expr)
