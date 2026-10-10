from typing import List, Sequence

from phalanx_language.datatypes import Float, Integer, Value
from phalanx_language.parser.ast import (BinaryOpNode, FloatLiteralNode,
                                         IntegerLiteralNode)
from phalanx_language.parser.ast.base import ASTNode

from . import arithmatic


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

            # Binary Operation
            case BinaryOpNode() as expr:
                return arithmatic.eval_binary(self, expr)
