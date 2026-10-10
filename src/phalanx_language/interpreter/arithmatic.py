from typing import TYPE_CHECKING

from phalanx_language.datatypes.base import Value
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.infix import BinaryOpNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def eval_binary(interpreter: Interpreter, expr: BinaryOpNode) -> Value:
    left = interpreter.evaluate(expr.left)
    right = interpreter.evaluate(expr.right)

    match expr.operator.type:
        case TokenTypes.PLUS:
            return left + right

        case TokenTypes.MINUS:
            return left - right

        case TokenTypes.MULT:
            return left * right

        case TokenTypes.DIV:
            return left / right

        case TokenTypes.MODULO:
            return left % right

        case _:
            raise Exception("Operator not found")
