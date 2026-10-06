from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Optional


class TokenTypes:
    EOF = auto()

    LPAREN = auto()
    RPAREN = auto()

    INT = auto()
    FLOAT = auto()

    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()
    MODULO = auto()


@dataclass
class Position:
    start: int
    end: int
    line: int
    column: int


class Token:
    def __init__(
        self, token_type: TokenTypes, value: Optional[Any], pos: Position
    ) -> None:
        self.type = token_type
        self.value = value
        self.pos = pos

    def __repr__(self) -> str:
        return f"{self.type}:{self.value}"
