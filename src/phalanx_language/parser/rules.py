from typing import TYPE_CHECKING

from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.binding_power import BindingPower
from phalanx_language.parser.infixs.binop import parse_binary_op
from phalanx_language.parser.prefixs.control_flow import parse_if_stmt
from phalanx_language.parser.prefixs.grouping import (parse_grouping_curly,
                                                      parse_grouping_paren)
from phalanx_language.parser.prefixs.lists import parse_lists
from phalanx_language.parser.prefixs.literals import parse_float, parse_int
from phalanx_language.parser.prefixs.unary import parse_unary
from phalanx_language.parser.prefixs.variables import (
    parse_identifier, parse_variable_declaration)
from phalanx_language.parser.types import InfixFn, PrefixFn

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


def register_all_rules(parser: Parser):
    def prefix(tok_type: TokenTypes, func: PrefixFn):
        parser.prefix_funcs[tok_type] = func

    def infix(tok_type: TokenTypes, func: InfixFn, bp: BindingPower):
        parser.infix_funcs[tok_type] = func
        parser.binding_powers[tok_type] = bp

    # Prefix Functions
    prefix(TokenTypes.LPAREN, parse_grouping_paren)
    prefix(TokenTypes.LCURLY, parse_grouping_curly)

    # Literals
    prefix(TokenTypes.INT, parse_int)
    prefix(TokenTypes.FLOAT, parse_float)
    prefix(TokenTypes.LBRACKET, parse_lists)

    # Unary
    prefix(TokenTypes.MINUS, parse_unary)
    prefix(TokenTypes.PLUS, parse_unary)

    # Variables
    prefix(TokenTypes.LET, parse_variable_declaration)
    prefix(TokenTypes.IDENTIFIER, parse_identifier)

    # Logical
    prefix(TokenTypes.NOT, parse_unary)

    # Control Floww
    prefix(TokenTypes.IF, parse_if_stmt)

    # Infix Functions

    infix(TokenTypes.EOF, parse_binary_op, BindingPower.NONE)

    # Arithmatics
    infix(TokenTypes.PLUS, parse_binary_op, BindingPower.SUM)
    infix(TokenTypes.MINUS, parse_binary_op, BindingPower.SUM)
    infix(TokenTypes.MULT, parse_binary_op, BindingPower.PRODUCT)
    infix(TokenTypes.DIV, parse_binary_op, BindingPower.PRODUCT)
    infix(TokenTypes.MODULO, parse_binary_op, BindingPower.PRODUCT)

    # Comparisions
    infix(TokenTypes.EQ, parse_binary_op, BindingPower.COMPARISON)
    infix(TokenTypes.NEQ, parse_binary_op, BindingPower.COMPARISON)
    infix(TokenTypes.GT, parse_binary_op, BindingPower.COMPARISON)
    infix(TokenTypes.GTE, parse_binary_op, BindingPower.COMPARISON)
    infix(TokenTypes.LT, parse_binary_op, BindingPower.COMPARISON)
    infix(TokenTypes.LTE, parse_binary_op, BindingPower.COMPARISON)

    # Logical
    infix(TokenTypes.OR, parse_binary_op, BindingPower.LOGICAL_OR)
    infix(TokenTypes.AND, parse_binary_op, BindingPower.LOGICAL_AND)
