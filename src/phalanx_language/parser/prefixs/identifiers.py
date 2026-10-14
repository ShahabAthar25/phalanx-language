from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.functions import FunctionCallNode
from phalanx_language.parser.ast.variables import (VariableAccessNode,
                                                   VariableAssignNode)

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_identifier(parser: Parser) -> ExpressionNode:
    tok = parser.current_tok

    parser.advance()

    # Variable assignment
    if parser.current_tok.type == TokenTypes.ASSIGN:
        parser.advance()  # Advances '=' to start of the expression

        expr = parser.parse_expr()

        return VariableAssignNode(tok, expr)

    elif parser.current_tok.type == TokenTypes.LPAREN:
        parser.advance()

        args = []

        while parser.current_tok.type != TokenTypes.RPAREN:
            arg = parser.parse_expr()

            args.append(arg)

            if parser.current_tok.type == TokenTypes.COMMA:
                parser.advance()
                continue

        parser.advance()

        return FunctionCallNode(tok, args)

    return VariableAccessNode(tok)
