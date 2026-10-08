from typing import Dict, Iterator

from phalanx_language.lexer.tokens import Position, Token, TokenTypes
from phalanx_language.parser.ast.base import ExpressionNode
from phalanx_language.parser.binding_power import BindingPower
from phalanx_language.parser.rules import register_all_rules
from phalanx_language.parser.types import InfixFn, PrefixFn

# A reusable EOF sentinel token
EOF_TOKEN = Token(TokenTypes.EOF, value=None, pos=Position(-1, -1, -1, -1))


class Parser:
    def __init__(self, tokens: Iterator[Token]) -> None:
        self.tokens = tokens

        self.current_tok: Token = next(self.tokens)

        self.prefix_funcs: Dict[TokenTypes, PrefixFn] = {}
        self.infix_funcs: Dict[TokenTypes, InfixFn] = {}
        self.binding_powers: Dict[TokenTypes, BindingPower] = {}

        if self.current_tok.type == TokenTypes.EOF:
            # Assign peak tok EOF as well to cleanly identify end of file
            self.peek_tok = EOF_TOKEN
        else:
            self.peek_tok: Token = next(self.tokens, EOF_TOKEN)

        register_all_rules(self)

    def advance(self):
        self.current_tok = self.peek_tok
        self.peek_tok = next(self.tokens, EOF_TOKEN)

    def consume(self, tok_type: TokenTypes, err_msg: str):
        tok = self.current_tok

        if tok.type != tok_type:
            raise Exception(err_msg)

        self.advance()

        return tok

    def bp(self) -> BindingPower:
        return self.binding_powers.get(self.current_tok.type, BindingPower.NONE)

    def parse(self):
        ast: list[ExpressionNode] = []
        while self.current_tok.type != TokenTypes.EOF:
            expr = self.parse_expr()
            ast.append(expr)

        return ast

    def parse_expr(self, min_bp: BindingPower = BindingPower.NONE) -> ExpressionNode:
        prefix_func = self.prefix_funcs.get(self.current_tok.type, None)
        if not prefix_func:
            raise SyntaxError(
                f"Unexpected token for expression: {self.current_tok.type}"
            )

        # Parse the expr
        left = prefix_func(self)

        while min_bp < self.bp():
            infix_func = self.infix_funcs.get(self.current_tok.type, None)
            if not infix_func:
                break

            left = infix_func(self, left)

        return left
