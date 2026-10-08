from enum import IntEnum

from phalanx_language.lexer.tokens import Token, TokenTypes


class BindingPower(IntEnum):
    NONE = 0
    ASSIGN = 1  # =
    SUM = 2  # +, -
    PRODUCT = 3  # *, /, %
    PREFIX = 4  # -x, !x
