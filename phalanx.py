import sys

from phalanx_language.datatypes.null import Null
from phalanx_language.interpreter.interpreter import Interpreter
from phalanx_language.lexer.lexer import Lexer
from phalanx_language.parser.parser import Parser


def run(source: str) -> None:
    lexer = Lexer(source)

    tokens = lexer.tokenize()

    parser = Parser(tokens)

    ast_list = parser.parse()
    print(ast_list)

    # interpreter = Interpreter()
    #
    # interpreter.interpret(ast_list)


filename = sys.argv[1] if len(sys.argv) >= 2 else None
if filename is not None:
    with open(filename, "r") as file:
        source = file.read()
        run(source)
else:
    raise Exception("Only works with file right now")
