from typing import TYPE_CHECKING

import polars as pl

from phalanx_language.datatypes.vector import Vector
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.parser.ast.prefix import VectorLiteralNode

if TYPE_CHECKING:
    from phalanx_language.interpreter.interpreter import Interpreter


def evaluate(interpreter: Interpreter, node: VectorLiteralNode, env: Enviroment):
    exprs = []
    for expr in node.exprs:
        exprs.append(interpreter.evaluate(expr, env).value)

    return Vector(pl.Series(exprs))
