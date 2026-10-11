from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.variables import VariableDeclarationNode

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_variable_declaration(parser: Parser):
    parser.advance()

    identifier = parser.consume(TokenTypes.IDENTIFIER, "Expected identifier")

    parser.consume(TokenTypes.TYPE_ASCRIPTION, "Expected '::'")

    type_ = parser.consume(TokenTypes.IDENTIFIER, "Expected type")

    parser.consume(TokenTypes.ASSIGN, "Expected '='")

    expr = parser.parse_expr()

    return VariableDecrelationNode(identifier, type_, expr)
