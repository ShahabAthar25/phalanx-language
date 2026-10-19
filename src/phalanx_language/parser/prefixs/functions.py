from typing import TYPE_CHECKING, List

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.functions import (FunctionDeclerationNode,
                                                   FunctionParamsNode,
                                                   ReturnNode)
from phalanx_language.parser.prefixs.grouping import parse_grouping_curly

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_func(parser: Parser):
    parser.advance()

    name = parser.consume(TokenTypes.IDENTIFIER, "Expected identifier")

    parser.consume(TokenTypes.LPAREN, "Expected '('")

    params: List[ExpressionNode] = []
    while parser.current_tok.type != TokenTypes.RPAREN:
        param = parser.consume(TokenTypes.IDENTIFIER, "Expected identifier as argument")

        parser.consume(TokenTypes.TYPE_ASCRIPTION, "Expected '::'")

        var_type = parser.consume(TokenTypes.IDENTIFIER, "Expected variable type")

        if parser.current_tok.type == TokenTypes.COMMA:
            parser.advance()

        param_node = FunctionParamsNode(param, var_type)

        params.append(param_node)

    parser.advance()

    parser.consume(TokenTypes.ARROW, "Expected '->' to get return type of function")

    return_type = parser.consume(
        TokenTypes.IDENTIFIER, "Expected return type of function"
    )

    code_block = parse_grouping_curly(parser)

    return FunctionDeclerationNode(name, params, return_type, code_block)


def parse_return(parser: Parser):
    parser.advance()

    expr = None
    if parser.current_tok.type in parser.prefix_funcs.keys():
        expr = parser.parse_expr()

    return ReturnNode(expr)
