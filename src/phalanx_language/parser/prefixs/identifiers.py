from typing import TYPE_CHECKING, List

from phalanx_language.lexer.tokens import Token, TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.dot import DotNode
from phalanx_language.parser.ast.functions import FunctionCallNode
from phalanx_language.parser.ast.variables import (VariableAccessNode,
                                                   VariableAssignNode)
from phalanx_language.parser.prefixs.functions import parse_func

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_identifier(parser: Parser) -> ExpressionNode:
    tok = parser.current_tok

    parser.advance()

    # Variable assignment
    if parser.current_tok.type == TokenTypes.ASSIGN:
        parser.advance()  # Advances '=' to start of the expression

        expr = parser.parse_expr()

        node = VariableAssignNode(tok, expr)

    elif parser.current_tok.type == TokenTypes.LPAREN:
        node = parse_function_call(parser, tok)

    else:
        node = VariableAccessNode(tok)

    # Dot notation parsing
    while parser.current_tok.type == TokenTypes.DOT:
        parser.advance()

        attr_tok = parser.consume(
            TokenTypes.IDENTIFIER, "Expected identifier after dot '.'"
        )

        if parser.current_tok.type == TokenTypes.LPAREN:
            node = parse_function_call(parser, attr_tok, initial_args=[node])

        else:
            node = DotNode(node, attr_tok)

    return node


def parse_function_call(
    parser: Parser, tok: Token, initial_args: List[ExpressionNode] | None = None
):
    parser.advance()

    args = list(initial_args) if initial_args is not None else []

    while parser.current_tok.type != TokenTypes.RPAREN:
        arg = parser.parse_expr()

        args.append(arg)

        if parser.current_tok.type == TokenTypes.COMMA:
            parser.advance()
            continue

    parser.advance()

    return FunctionCallNode(tok, args)
