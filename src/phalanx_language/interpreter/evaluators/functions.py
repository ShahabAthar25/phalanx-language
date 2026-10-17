from typing import TYPE_CHECKING

from polars.datatypes import Null

from phalanx_language.datatypes.function import Function
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.interpreter.signals import ReturnSignal
from phalanx_language.parser.ast.functions import FunctionCallNode
from phalanx_language.parser.prefixs.grouping import parse_grouping_curly

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, node: FunctionCallNode, env: Enviroment):
    func_val = env.retrieve(node.name.value)

    if not isinstance(func_val, Function):
        raise TypeError(f"{node.name} is not callable")

    evaluated_args = [interpreter.evaluate(arg, env) for arg in node.args]

    if len(func_val.params) != len(evaluated_args):
        raise RuntimeError(f"Function {node.name} expects {len(evaluated_args)}")

    closure_env = Enviroment(parent=env)

    for param, arg in zip(func_val.params, evaluated_args):
        closure_env.define(param.name.value, arg, param.var_type.value)

    try:
        interpreter.interpret(func_val.code_block, env=closure_env, register=False)
        return Null()
    except ReturnSignal as ret:
        return ret.value
