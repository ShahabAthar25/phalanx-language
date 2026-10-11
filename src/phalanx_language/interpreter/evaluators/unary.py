from typing import TYPE_CHECKING

from phalanx_language.datatypes.bool import Boolean
from phalanx_language.datatypes.int import Integer
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.ast.infix import BinaryOpNode
from phalanx_language.parser.ast.prefix import UnaryNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, node: UnaryNode, env: Enviroment):
    match node.operator.type:
        # Unary
        case TokenTypes.PLUS:
            return interpreter.evaluate(node.expr, env)

        case TokenTypes.MINUS:
            return Integer(-1) * interpreter.evaluate(node.expr, env)

        # Logical
        case TokenTypes.NOT:
            val = interpreter.evaluate(node.expr, env)
            return Boolean(val.negate())

        case _:
            raise RuntimeError(f"Unexpected AST Node: {node}")
