from typing import TYPE_CHECKING, List

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.prefix import ListLiteralNode

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_lists(parser: Parser):
    parser.advance()

    # Empty List
    if parser.current_tok.type == TokenTypes.RBRACKET:
        parser.advance()  # Consume ']'
        return ListLiteralNode([])

    expr_list: List[ExpressionNode] = []
    while True:
        expr = parser.parse_expr()
        expr_list.append(expr)

        match parser.current_tok.type:
            case TokenTypes.COMMA:
                parser.advance()
                continue

            case TokenTypes.RBRACKET:
                parser.advance()
                break

            case _:
                raise SyntaxError("Expected ']'")

    return ListLiteralNode(items=expr_list)
