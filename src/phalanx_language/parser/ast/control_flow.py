from dataclasses import dataclass
from typing import List

from phalanx_language.parser.ast.base import ASTNode, ExpressionNode
from phalanx_language.parser.ast.infix import BinaryOpNode


@dataclass(frozen=True)
class IfStmtNode(ExpressionNode):
    condition: BinaryOpNode
    code_block: List[ASTNode]

    def __repr__(self) -> str:
        return f"if ({self.condition}) {self.code_block}"
