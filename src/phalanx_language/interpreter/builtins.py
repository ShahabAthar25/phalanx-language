from typing import TYPE_CHECKING

from phalanx_language.builtins.input import builtin_input
from phalanx_language.builtins.load_data import builtin_load_data
from phalanx_language.builtins.print import builtin_println
from phalanx_language.builtins.vectors import builtin_shift
from phalanx_language.datatypes.bool import Boolean
from phalanx_language.datatypes.builtinfunctions import BuiltInFunction
from phalanx_language.datatypes.null import Null

if TYPE_CHECKING:
    from phalanx_language.interpreter.environment import Enviroment


def register_builtins(env: Enviroment):
    # Null
    env.define("null", Null(), "null")

    # Booleans
    env.define("false", Boolean(False), "bool")
    env.define("true", Boolean(True), "bool")

    # Builtin Functions
    env.define_function("print", BuiltInFunction(builtin_println), "null")
    env.define_function("input", BuiltInFunction(builtin_input), "string")
    env.define_function("load_data", BuiltInFunction(builtin_load_data), "asset")
    env.define_function("shift", BuiltInFunction(builtin_shift), "vector")
