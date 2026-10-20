from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.match import ConditionNode, MatchNode

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_match(parser: Parser):
    parser.advance()

    parser.consume(TokenTypes.LCURLY, "Expected left bracket after match")

    condition_nodes = []
    while parser.current_tok.type not in (TokenTypes.RCURLY, TokenTypes.EOF):
        condition = parser.parse_expr()
        parser.consume(TokenTypes.FAT_ARROW, "Expected => after codition in match")
        value = parser.parse_expr()

        condition_nodes.append(ConditionNode(condition, value))

    parser.advance()

    return MatchNode(condition_nodes)
