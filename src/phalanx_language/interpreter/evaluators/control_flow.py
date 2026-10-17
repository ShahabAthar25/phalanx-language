from typing import TYPE_CHECKING

from phalanx_language.datatypes.null import Null
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.parser.ast.control_flow import IfStmtNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate_if_stmt(interpreter: Interpreter, node: IfStmtNode, env: Enviroment):
    condition = interpreter.evaluate(node.condition, env)

    if condition.is_truthy():
        result = interpreter.interpret(node.code_block, env=env, register=False)
    else:
        result = Null()

    return result
