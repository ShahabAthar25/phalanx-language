from typing import Generator, Iterable

from phalanx_language.lexer.tokens import Position, Token, TokenTypes

DIGITS = "1234567890"


class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text

        # For retrieving current char
        self.idx = 0

        # For error handling
        self.col_idx = 1
        self.line = 1

        self.current_char: str | None = (
            self.text[self.idx] if len(self.text) > 0 else None
        )

    def advance(self):
        if self.current_char == "\n":
            self.line += 1
            self.col_idx = 1
        else:
            self.col_idx += 1

        self.idx += 1

        if (len(self.text) - 1) >= self.idx:
            self.current_char = self.text[self.idx]

        else:
            self.current_char = None

    def tokenize(self) -> Generator[Token]:
        while self.current_char:

            if self.current_char in " \t":
                self.advance()

            elif self.current_char == "\n":
                # Moved logic to advance as is more useful but still kept if statement as
                # might need it for making language multiline
                self.advance()

            elif self.current_char == "+":
                yield Token(
                    TokenTypes.PLUS,
                    Position(self.idx, self.idx + 1, self.line, self.col_idx),
                )
                self.advance()

            elif self.current_char == "-":
                yield Token(
                    TokenTypes.MINUS,
                    Position(self.idx, self.idx + 1, self.line, self.col_idx),
                )
                self.advance()

            elif self.current_char == "*":
                yield Token(
                    TokenTypes.MULT,
                    Position(self.idx, self.idx + 1, self.line, self.col_idx),
                )
                self.advance()

            elif self.current_char == "/":
                yield Token(
                    TokenTypes.DIV,
                    Position(self.idx, self.idx + 1, self.line, self.col_idx),
                )
                self.advance()

            elif self.current_char == "%":
                yield Token(
                    TokenTypes.MODULO,
                    Position(self.idx, self.idx + 1, self.line, self.col_idx),
                )
                self.advance()

            elif self.current_char in DIGITS:
                yield self.make_number()

        yield Token(
            TokenTypes.EOF, Position(self.idx, self.idx, self.line, self.col_idx)
        )

    def make_number(self) -> Token:
        decimal = False
        num = ""
        start_idx = self.idx
        start_col = self.col_idx

        while self.current_char and self.current_char in DIGITS + "._":

            if self.current_char == "_":
                # Only for reading no acutual meaning
                self.advance()
                continue

            elif self.current_char == ".":
                decimal = True

            num += self.current_char
            self.advance()

        token_type = TokenTypes.FLOAT if decimal else TokenTypes.INT
        val = float(num) if decimal else int(num)

        return Token(
            token_type,
            value=val,
            pos=Position(start_idx, self.idx, self.line, start_col),
        )
