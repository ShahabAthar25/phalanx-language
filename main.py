from phalanx_language.interpreter.interpreter import Interpreter
from phalanx_language.lexer.lexer import Lexer
from phalanx_language.parser.ast import (ASTNode, BinaryOpNode,
                                         IntegerLiteralNode, LiteralNode)
from phalanx_language.parser.parser import Parser

source = "17%3"
lexer = Lexer(source)

tokens = lexer.tokenize()

parser = Parser(tokens)

ast_list = parser.parse()

interpreter = Interpreter()
val = interpreter.interpret(ast_list)

if val is not None:
    print(val)
