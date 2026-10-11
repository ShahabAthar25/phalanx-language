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
    print(ast_list)

    # interpreter = Interpreter()
    # val = interpreter.interpret(ast_list)
    #
    # if val is not None:
    #     print(val)


# source = "6 * -6 <= 5 * 6 or 0"
while True:
    source = input(">>> ")
    run(source)
