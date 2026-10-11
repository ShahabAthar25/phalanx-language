from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.binding_power import BindingPower

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_grouping(parser: Parser):
    parser.advance()

    # Handle edge-case: Empty parenthesis (). () are not allowed
    if parser.current_tok.type == TokenTypes.RPAREN:
        raise SyntaxError('Unexpected empty parentheses "()"')

    expr = parser.parse_expr(BindingPower.NONE)

    parser.consume(TokenTypes.RPAREN, 'Expected ")"')

    return expr
