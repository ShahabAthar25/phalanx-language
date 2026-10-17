from phalanx_language.datatypes.null import Null
from phalanx_language.interpreter.interpreter import Interpreter
from phalanx_language.lexer.lexer import Lexer
from phalanx_language.parser.ast import (ASTNode, BinaryOpNode,
                                         IntegerLiteralNode, LiteralNode)
from phalanx_language.parser.parser import Parser


def run(source: str) -> None:
    lexer = Lexer(source)

    tokens = lexer.tokenize()

    parser = Parser(tokens)

    ast_list = parser.parse()

    interpreter = Interpreter()

    val = interpreter.interpret(ast_list)

    if not isinstance(val, Null):
        print(val)


source = """
let a::vector = [1,2,3]
let b::vector = [1,2,3]
a+b
"""
run(source)
# while True:
#     source = input(">>> ")
#     run(source)
