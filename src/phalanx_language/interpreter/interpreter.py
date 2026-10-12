from typing import List, Sequence

from phalanx_language.datatypes import Float, Integer, Value
from phalanx_language.datatypes.null import Null
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast import (BinaryOpNode, FloatLiteralNode,
                                         IntegerLiteralNode,
                                         VariableDeclarationNode)
from phalanx_language.parser.ast.base import ASTNode
from phalanx_language.parser.ast.prefix import UnaryNode
from phalanx_language.parser.ast.variables import VariableAccessNode

from .builtins import register_builtins
from .evaluators import arithmatic, logicals, unary


class Interpreter:
    def interpret(self, ast_list: Sequence[ASTNode]) -> Value | None:
        last_evaluated_value = None
        env = Enviroment()
        register_builtins(env)

        for stmt in ast_list:
            last_evaluated_value = self.evaluate(stmt, env)

        return last_evaluated_value

    def evaluate(self, node: ASTNode, env: Enviroment) -> Value:
        match node:
            # Literals
            case IntegerLiteralNode(value=val):
                return Integer(value=val)
            case FloatLiteralNode(value=val):
                return Float(value=val)
            case UnaryNode() as expr:
                return unary.evaluate(self, expr, env)

            # Binary Operation
            case BinaryOpNode() as expr:
                match expr.operator.type:
                    case (
                        TokenTypes.PLUS
                        | TokenTypes.MINUS
                        | TokenTypes.MULT
                        | TokenTypes.DIV
                    ):
                        return arithmatic.evaluate(self, expr, env)

                    case (
                        TokenTypes.EQ
                        | TokenTypes.NEQ
                        | TokenTypes.GT
                        | TokenTypes.GTE
                        | TokenTypes.LT
                        | TokenTypes.LTE
                    ):
                        return logicals.evaluate_comparison(self, expr, env)

                    case TokenTypes.OR | TokenTypes.AND:
                        return logicals.evaluate_logical(self, expr, env)

                    case _:
                        raise RuntimeError(
                            f"Unknown binary operator: {expr.operator.type}"
                        )

            # Variables
            case VariableDeclarationNode(identifier, var_type, expr):
                env.define(identifier.value, self.evaluate(expr, env), var_type.value)
                return Null()

            case VariableAccessNode(identifier):
                var = env.retrieve(identifier.value)
                return var

            case _:
                raise RuntimeError(f"Exexpected ast node: {node}")
