from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.binding_power import BindingPower
from phalanx_language.parser.infixs.binop import parse_binary_op
from phalanx_language.parser.prefixs.literals import parse_float, parse_int
from phalanx_language.parser.types import InfixFn, PrefixFn

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def register_all_rules(parser: Parser):
    def prefix(tok_type: TokenTypes, func: PrefixFn):
        parser.prefix_funcs[tok_type] = func

    def infix(tok_type: TokenTypes, func: InfixFn, bp: BindingPower):
        parser.infix_funcs[tok_type] = func
        parser.binding_powers[tok_type] = bp

    # Literals
    prefix(TokenTypes.INT, parse_int)
    prefix(TokenTypes.FLOAT, parse_float)

    # Unary
    # To be implemented
    # prefix(TokenTypes.MINUS, parse_unary)
    # prefix(TokenTypes.PLUS, parse_unary)

    # Infix Functions
    infix(TokenTypes.EOF, parse_binary_op, BindingPower.NONE)
    infix(TokenTypes.PLUS, parse_binary_op, BindingPower.SUM)
    infix(TokenTypes.MINUS, parse_binary_op, BindingPower.SUM)
    infix(TokenTypes.MULT, parse_binary_op, BindingPower.PRODUCT)
    infix(TokenTypes.DIV, parse_binary_op, BindingPower.PRODUCT)
    infix(TokenTypes.MODULO, parse_binary_op, BindingPower.PRODUCT)
