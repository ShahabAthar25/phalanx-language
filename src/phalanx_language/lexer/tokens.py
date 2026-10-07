from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Optional


class TokenTypes(StrEnum):
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
    start_idx: int
    end_idx: int
    line: int
    col: int


class Token:
    def __init__(
        self,
        token_type: TokenTypes,
        pos: Position,
        value: Optional[Any] = None,
    ) -> None:
        self.type = token_type
        self.value = value
        self.pos = pos

    def __repr__(self) -> str:
        if self.value:
            return f"{self.type}:{self.value}"

        return f"{self.type}"
