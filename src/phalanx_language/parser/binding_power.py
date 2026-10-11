from enum import IntEnum

from phalanx_language.lexer.tokens import Token, TokenTypes


class BindingPower(IntEnum):
    NONE = 0
    ASSIGN = 1  # =
    LOGICAL_OR = 2
    LOGICAL_AND = 3
    COMPARISON = 4  # ==, !=, <=, <, >=, >
    SUM = 5  # +, -
    PRODUCT = 6  # *, /, %
    PREFIX = 7  # -x
