from typing import Generator, Iterable

from phalanx_language.lexer.tokens import KEYWORDS, Position, Token, TokenTypes

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
            match self.current_char:
                case " " | "\t":
                    self.advance()

                case "\n":
                    # Moved logic to advance as is more useful but still kept if statement as
                    # might need it for making language multiline
                    self.advance()

                case "(":
                    yield Token(
                        TokenTypes.LPAREN,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case ")":
                    yield Token(
                        TokenTypes.RPAREN,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "{":
                    yield Token(
                        TokenTypes.LCURLY,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "}":
                    yield Token(
                        TokenTypes.RCURLY,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "[":
                    yield Token(
                        TokenTypes.LBRACKET,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "]":
                    yield Token(
                        TokenTypes.RBRACKET,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "+":
                    yield Token(
                        TokenTypes.PLUS,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "-":
                    yield Token(
                        TokenTypes.MINUS,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "*":
                    yield Token(
                        TokenTypes.MULT,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "/":
                    yield Token(
                        TokenTypes.DIV,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case "%":
                    yield Token(
                        TokenTypes.MODULO,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case ",":
                    yield Token(
                        TokenTypes.COMMA,
                        Position(self.idx, self.idx + 1, self.line, self.col_idx),
                    )
                    self.advance()

                case ":":
                    yield self.make_compount_token(
                        TokenTypes.TYPE_ASCRIPTION, TokenTypes.COLON, ":"
                    )

                case "=":
                    yield self.make_compount_token(TokenTypes.EQ, TokenTypes.ASSIGN)

                case "!":
                    yield self.make_neq()

                case ">":
                    yield self.make_compount_token(TokenTypes.GTE, TokenTypes.GT)

                case "<":
                    yield self.make_compount_token(TokenTypes.LTE, TokenTypes.LT)

                case char if char in DIGITS:
                    yield self.make_number()

                case char if char.isalpha():
                    yield self.make_identifier_or_keyword()

                case _:
                    raise SyntaxError(
                        f"Unexpected character: '{self.current_char}' at line {self.line}, col {self.col_idx}"
                    )

        yield Token(
            TokenTypes.EOF, Position(self.idx, self.idx, self.line, self.col_idx)
        )

    def make_compount_token(
        self, tok_type_1: TokenTypes, tok_type_2: TokenTypes, next_char: str = "="
    ):
        start_idx = self.idx
        start_col = self.col_idx

        self.advance()

        if self.current_char == next_char:
            tok_type = tok_type_1
            self.advance()
        else:
            tok_type = tok_type_2

        return Token(tok_type, pos=Position(start_idx, self.idx, self.line, start_col))

    def make_neq(self):
        start_idx = self.idx
        start_col = self.col_idx

        self.advance()

        if self.current_char != "=":
            raise SyntaxError("Expected '=' after '!'")

        self.advance()

        return Token(
            TokenTypes.NEQ, pos=Position(start_idx, self.idx, self.line, start_col)
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
            raw_value=val,
            pos=Position(start_idx, self.idx, self.line, start_col),
        )

    def make_identifier_or_keyword(self):
        start_idx = self.idx
        start_col = self.col_idx
        value = ""

        while self.current_char and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            value += self.current_char
            self.advance()

        tok_type = KEYWORDS.get(value, TokenTypes.IDENTIFIER)

        return Token(
            tok_type,
            pos=Position(start_idx, self.idx, self.line, start_col),
            raw_value=value if tok_type == TokenTypes.IDENTIFIER else None,
        )
