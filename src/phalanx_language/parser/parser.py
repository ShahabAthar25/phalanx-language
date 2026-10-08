from typing import Iterator

from phalanx_language.lexer.tokens import Position, Token, TokenTypes

# A reusable EOF sentinel token
EOF_TOKEN = Token(TokenTypes.EOF, value=None, pos=Position(-1, -1, -1, -1))


class Parser:
    def __init__(self, tokens: Iterator[Token]) -> None:
        self.tokens = tokens

        self.current_tok: Token = next(self.tokens)

        if self.current_tok.type == TokenTypes.EOF:
            # Assign peak tok EOF as well to cleanly identify end of file
            self.peek_tok = EOF_TOKEN
        else:
            self.peek_tok: Token = next(self.tokens, EOF_TOKEN)

    def advance(self):
        self.current_tok = self.peek_tok
        self.peek_tok = next(self.tokens, EOF_TOKEN)

    def consume(self, tok_type: TokenTypes, err_msg: str):
        tok = self.current_tok

        if tok.type != tok_type:
            raise Exception(err_msg)

        self.advance()

        return tok

    def parse(self):
        while self.current_tok.type != TokenTypes.EOF:
            self.parse_expr()

    def parse_expr(self):
        self.advance()
