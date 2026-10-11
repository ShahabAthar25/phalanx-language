from typing import List, Sequence

from phalanx_language.datatypes import Float, Integer, Value
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast import (BinaryOpNode, FloatLiteralNode,
                                         IntegerLiteralNode)
from phalanx_language.parser.ast.base import ASTNode
from phalanx_language.parser.ast.prefix import UnaryNode

from . import arithmatic, logicals


class Interpreter:
    def interpret(self, ast_list: Sequence[ASTNode]) -> Value | None:
        last_evaluated_value = None

        for stmt in ast_list:
            last_evaluated_value = self.evaluate(stmt)

        return last_evaluated_value

    def evaluate(self, node: ASTNode) -> Value:
        match node:
            # Literals
            case IntegerLiteralNode(value=val):
                return Integer(value=val)
            case FloatLiteralNode(value=val):
                return Float(value=val)
            case UnaryNode(operator, expr):
                sign = Integer(-1) if operator.type == TokenTypes.MINUS else Integer(1)
                expr = self.evaluate(expr)
                return sign * expr

            # Binary Operation
            case BinaryOpNode() as expr:
                match expr.operator.type:
                    case (
                        TokenTypes.PLUS
                        | TokenTypes.MINUS
                        | TokenTypes.MULT
                        | TokenTypes.DIV
                    ):
                        return arithmatic.evaluate(self, expr)

                    case (
                        TokenTypes.EQ
                        | TokenTypes.NEQ
                        | TokenTypes.GT
                        | TokenTypes.GTE
                        | TokenTypes.LT
                        | TokenTypes.LTE
                    ):
                        return logicals.evaluate(self, expr)

                    case _:
                        raise RuntimeError(
                            f"Unknown binary operator: {expr.operator.type}"
                        )
            case _:
                raise RuntimeError(f"Exexpected ast node: {node}")
