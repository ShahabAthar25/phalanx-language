from typing import TYPE_CHECKING

from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.infix import BinaryOpNode
from phalanx_language.parser.binding_power import BindingPower

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def parse_binary_op(parser: Parser, left: ExpressionNode) -> ExpressionNode:
    op_token = parser.current_tok

    current_bp = parser.binding_powers.get(op_token.type, BindingPower.NONE)

    # Advance on to rhs expr
    parser.advance()

    # recursion
    right = parser.parse_expr(min_bp=current_bp)

    return BinaryOpNode(left=left, operator=op_token, right=right)
