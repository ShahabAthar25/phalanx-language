from dataclasses import dataclass
from typing import List

from phalanx_language.parser.ast.base import ExpressionNode


@dataclass(frozen=True, slots=True)
class MatchNode(ExpressionNode):
    exprs: List[ConditionNode]

    def __repr__(self) -> str:
        return f"match {self.exprs}"


@dataclass(frozen=True, slots=True)
class ConditionNode(ExpressionNode):
    condition: ExpressionNode
    value: ExpressionNode

    def __repr__(self) -> str:
        return f"{self.condition}=>{self.value}"
