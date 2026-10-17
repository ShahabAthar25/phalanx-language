from typing import TYPE_CHECKING

from phalanx_language.parser.ast.prefix import (FloatLiteralNode,
                                                IntegerLiteralNode,
                                                StringLiteralNode)

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_int(parser: Parser):
    node = IntegerLiteralNode(parser.current_tok)

    parser.advance()

    return node


def parse_float(parser: Parser):
    node = FloatLiteralNode(parser.current_tok)

    parser.advance()

    return node


def parse_string(parser: Parser):
    node = StringLiteralNode(parser.current_tok)

    parser.advance()

    return node
