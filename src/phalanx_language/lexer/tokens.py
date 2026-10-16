from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Optional


class TokenTypes(StrEnum):
    EOF = auto()

    LPAREN = auto()
    RPAREN = auto()

    LCURLY = auto()
    RCURLY = auto()

    LBRACKET = auto()
    RBRACKET = auto()

    # Literals
    INT = auto()
    FLOAT = auto()

    # Arithmatic
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()
    MODULO = auto()

    # Assignments
    ASSIGN = auto()  # '='

    # Logical
    EQ = auto()  # '=='
    NEQ = auto()
    GT = auto()
    GTE = auto()
    LT = auto()
    LTE = auto()

    # Conditions
    NOT = auto()
    OR = auto()
    AND = auto()

    # Variables
    LET = auto()

    # Types
    TYPE_ASCRIPTION = auto()

    # Control Flow
    IF = auto()

    # Functions
    FUNC = auto()

    # Identifiers
    IDENTIFIER = auto()

    # Maps
    COLON = auto()
    COMMA = auto()


KEYWORDS = {
    "not": TokenTypes.NOT,
    "or": TokenTypes.OR,
    "and": TokenTypes.AND,
    "let": TokenTypes.LET,
    "if": TokenTypes.IF,
    "func": TokenTypes.FUNC,
}


@dataclass
class Position:
    start_idx: int
    end_idx: int
    line: int
    col: int


@dataclass(frozen=True)
class Token:
    type: TokenTypes
    pos: Position
    raw_value: Optional[Any] = None

    @property
    def value(self):
        if not self.raw_value:
            raise RuntimeError(f"No value found in token {self.type}")

        return self.raw_value

    def __repr__(self) -> str:
        if self.value is not None:
            return f"{self.type}:{self.value}"

        return f"{self.type}"
