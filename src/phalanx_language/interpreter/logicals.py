from typing import TYPE_CHECKING

from phalanx_language.datatypes.bool import Boolean
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.infix import BinaryOpNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, expr: BinaryOpNode):
    left = interpreter.evaluate(expr.left)
    right = interpreter.evaluate(expr.right)

    match expr.operator.type:
        case TokenTypes.EQ:
            return Boolean(left.value == right.value)

        case TokenTypes.NEQ:
            return Boolean(left.value != right.value)

        case TokenTypes.GT:
            return Boolean(left.value > right.value)

        case TokenTypes.GTE:
            return Boolean(left.value >= right.value)

        case TokenTypes.LT:
            return Boolean(left.value < right.value)

        case TokenTypes.LTE:
            return Boolean(left.value <= right.value)

        case _:
            raise RuntimeError(f"Unexpected logical operator: {expr.operator}")
