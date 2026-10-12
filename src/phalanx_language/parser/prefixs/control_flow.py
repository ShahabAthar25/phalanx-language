from typing import TYPE_CHECKING, List

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ASTNode
from phalanx_language.parser.ast.control_flow import IfStmtNode
from phalanx_language.parser.prefixs.grouping import parse_grouping_curly

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_if_stmt(parser: Parser):
    parser.advance()

    condition = parser.parse_expr()

    code_block = parse_grouping_curly(parser)

    return IfStmtNode(condition, code_block)
