from typing import TYPE_CHECKING

import polars as pl

from phalanx_language.datatypes.vector import Vector
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.parser.ast.match import MatchNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, node: MatchNode, env: Enviroment):
    when_chain = None

    for condition_node in node.exprs:
        condition = interpreter.evaluate(condition_node.condition, env)
        value = interpreter.evaluate(condition_node.value, env)

        if when_chain is None:
            when_chain = pl.when(condition.value).then(value.value)
        else:
            when_chain = when_chain.when(condition.value).then(value.value)

    result = pl.select(when_chain).to_series()

    return Vector(result)
