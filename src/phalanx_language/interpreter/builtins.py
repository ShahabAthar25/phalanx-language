from typing import TYPE_CHECKING

from phalanx_language.datatypes.bool import Boolean
from phalanx_language.datatypes.null import Null

if TYPE_CHECKING:
    from phalanx_language.interpreter.environment import Enviroment


def register_builtins(env: Enviroment):
    # Null
    env.define("null", Null(), "null")

    # Booleans
    env.define("false", Boolean(False), "bool")
    env.define("true", Boolean(True), "bool")
