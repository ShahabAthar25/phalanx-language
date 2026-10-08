from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from phalanx_language.parser.ast import ExpressionNode

if TYPE_CHECKING:
    from phalanx_language.parser.parser import Parser


# Prefix handler signature: takes Parser, returns ExpressionNode
PrefixFn = Callable[["Parser"], ExpressionNode]

# Infix handler signature: takes Parser and left ExpressionNode, returns ExpressionNode
InfixFn = Callable[["Parser", ExpressionNode], ExpressionNode]
