from typing import TYPE_CHECKING

from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.parser.ast.dot import DotNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, node: DotNode, env: Enviroment):
    left = interpreter.evaluate(node.left, env)
    attr = node.attr.value

    return left.get_attribute(attr)
