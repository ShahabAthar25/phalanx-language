from phalanx_language.lexer.lexer import Lexer

source = "1234567890 + 1234567890"
lexer = Lexer(source)

tokens = lexer.tokenize()

for token in tokens:
    print(token)
