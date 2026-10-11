from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.prefix import UnaryNode
from phalanx_language.parser.binding_power import BindingPower

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_unary(parser: Parser):
    operator = parser.current_tok

    parser.advance()

    expr = parser.parse_expr(BindingPower.PREFIX)

    return UnaryNode(operator, expr)
