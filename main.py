from phalanx_language.lexer.lexer import Lexer
from phalanx_language.parser.ast import (ASTNode, BinaryOpNode,
                                         IntegerLiteralNode, LiteralNode)
from phalanx_language.parser.parser import Parser

source = "28 + 29 - 93 * 83 / 9"
lexer = Lexer(source)

tokens = lexer.tokenize()

parser = Parser(tokens)

ast = parser.parse()
print(ast)
