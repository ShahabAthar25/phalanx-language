from typing import TYPE_CHECKING

from phalanx_language.datatypes.bool import Boolean
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.infix import BinaryOpNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate_comparison(interpreter: Interpreter, node: BinaryOpNode, env):
    left = interpreter.evaluate(node.left, env)
    right = interpreter.evaluate(node.right, env)

    match node.operator.type:
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
            raise RuntimeError(f"Unexpected logical operator: {node.operator}")


def evaluate_logical(interpreter: Interpreter, node: BinaryOpNode, env: Enviroment):
    left = interpreter.evaluate(node.left, env)
    right = interpreter.evaluate(node.right, env)

    match node.operator.type:
        case TokenTypes.OR:
            if left.is_truthy():
                return Boolean(True)

            return Boolean(True) if right.is_truthy() else Boolean(False)

        case TokenTypes.AND:
            if not left.is_truthy():
                return left

            return Boolean(True) if right.is_truthy() else Boolean(False)

        case _:
            raise RuntimeError(f"Unexpected node: {node} expected 'and' or 'or'")
