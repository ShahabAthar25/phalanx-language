from typing import List, Optional, Sequence

from phalanx_language.datatypes import Float, Integer, Value
from phalanx_language.datatypes.function import Function
from phalanx_language.datatypes.null import Null
from phalanx_language.datatypes.strings import String
from phalanx_language.interpreter.environment import Enviroment
from phalanx_language.interpreter.signals import ReturnSignal
from phalanx_language.lexer.tokens import TokenTypes
from phalanx_language.parser.ast import (BinaryOpNode, FloatLiteralNode,
                                         IntegerLiteralNode,
                                         VariableDeclarationNode)
from phalanx_language.parser.ast.base import ASTNode, ExpressionNode
from phalanx_language.parser.ast.control_flow import IfStmtNode
from phalanx_language.parser.ast.dot import DotNode
from phalanx_language.parser.ast.functions import (FunctionCallNode,
                                                   FunctionDeclerationNode,
                                                   ReturnNode)
from phalanx_language.parser.ast.prefix import (NullNode, StringLiteralNode,
                                                UnaryNode, VectorLiteralNode)
from phalanx_language.parser.ast.variables import (VariableAccessNode,
                                                   VariableAssignNode)

from .builtins import register_builtins
from .evaluators import (arithmatic, control_flow, dot, functions, logicals,
                         unary, vectors)


class Interpreter:
    def interpret(
        self,
        ast_list: Sequence[ASTNode],
        env_parent: Optional[Enviroment] = None,
        env: Optional[Enviroment] = None,
        register: bool = True,
    ) -> Value:
        last_evaluated_value = Null()

        if not env:
            env = Enviroment(parent=env_parent)

            if register:
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
            case StringLiteralNode(value=val):
                return String(value=val)
            case UnaryNode() as node:
                return unary.evaluate(self, node, env)
            case VectorLiteralNode() as node:
                return vectors.evaluate(self, node, env)

            # Dot notation
            case DotNode() as node:
                return dot.evaluate(self, node, env)

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

            case VariableAssignNode(identifier, expr):
                expr_evaluated = self.evaluate(expr, env)
                env.assign(identifier.value, expr_evaluated)
                return expr_evaluated

            case VariableAccessNode(identifier):
                var = env.retrieve(identifier.value)
                return var

            # Functions
            case FunctionDeclerationNode(name, params, return_type, code_block):
                func = Function(name.value, params, return_type.value, code_block, env)
                env.define_function(name.value, func, return_type.value)
                return func

            case FunctionCallNode() as node:
                return functions.evaluate(self, node, env)

            case ReturnNode(expr):
                value = self.evaluate(expr, env) if expr is not None else Null()
                raise ReturnSignal(value)

            # Control Flow
            case IfStmtNode() as node:
                return control_flow.evaluate_if_stmt(self, node, env)

            case _:
                raise RuntimeError(f"Exexpected ast node: {node}")
