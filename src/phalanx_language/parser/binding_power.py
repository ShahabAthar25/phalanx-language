from enum import IntEnum

from phalanx_language.lexer.tokens import Token, TokenTypes


class BindingPower(IntEnum):
    NONE = 0
    ASSIGN = 1  # =
    COND = 2  # ==, !=, <=, <, >=, >
    SUM = 3  # +, -
    PRODUCT = 4  # *, /, %
    PREFIX = 5  # -x, !x
