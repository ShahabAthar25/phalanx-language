from typing import TYPE_CHECKING, List

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.prefix import NullNode
from phalanx_language.parser.binding_power import BindingPower

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_grouping_paren(parser: Parser):
    parser.advance()

    # Handle edge-case: Empty parenthesis (). () are not allowed
    if parser.current_tok.type == TokenTypes.RPAREN:
        raise SyntaxError('Unexpected empty parentheses "()"')

    expr = parser.parse_expr(BindingPower.NONE)

    parser.consume(TokenTypes.RPAREN, 'Expected ")"')

    return expr


def parse_grouping_curly(parser: Parser) -> List[ExpressionNode]:
    parser.advance()

    # Empty code block should return nothing
    if parser.current_tok.type == TokenTypes.RCURLY:
        return []

    statements = []
    while (
        parser.current_tok.type != TokenTypes.RCURLY
        and parser.current_tok.type != TokenTypes.EOF
    ):
        stmt = parser.parse_expr()
        statements.append(stmt)

    parser.consume(TokenTypes.RCURLY, 'Expected "}"')

    return statements
