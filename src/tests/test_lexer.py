from phalanx_language.lexer.lexer import Lexer
from phalanx_language.lexer.tokens import TokenTypes


def test_advance():
    source = "1 + 1"
    lexer = Lexer(source)

    assert lexer.current_char == "1", f"For {lexer.idx}, {lexer.current_char}"
    assert lexer.idx == 0

    lexer.advance()

    assert lexer.current_char == " ", f"For {lexer.idx}, {lexer.current_char}"
    assert lexer.idx == 1

    lexer.advance()

    assert lexer.current_char == "+", f"For {lexer.idx}, {lexer.current_char}"
    assert lexer.idx == 2

    lexer.advance()

    assert lexer.current_char == " ", f"For {lexer.idx}, {lexer.current_char}"
    assert lexer.idx == 3

    lexer.advance()

    assert lexer.current_char == "1", f"For {lexer.idx}, {lexer.current_char}"
    assert lexer.idx == 4


def test_new_line_col_resey():
    lexer = Lexer("1\n1")

    assert lexer.col_idx == 1

    # Advance two times as \n should be ignored and col_idx should be 1
    # on new line and not 1 on \n
    lexer.advance()
    lexer.advance()

    assert lexer.col_idx == 1


def test_basic_expression_tokens():
    source = "1+1-1*1/1"
    lexer = Lexer(source)
    tokens = list(lexer.tokenize())

    expected_types = [
        TokenTypes.INT,
        TokenTypes.PLUS,
        TokenTypes.INT,
        TokenTypes.MINUS,
        TokenTypes.INT,
        TokenTypes.MULT,
        TokenTypes.INT,
        TokenTypes.DIV,
        TokenTypes.INT,
        TokenTypes.EOF,  # Includes EOF
    ]

    assert len(tokens) == len(expected_types)

    for token, expected_type in zip(tokens, expected_types):
        assert token.type == expected_type


def test_empty_input_yields_eof():
    lexer = Lexer("")
    tokens = list(lexer.tokenize())

    assert len(tokens) == 1
    assert tokens[0].type == TokenTypes.EOF
    assert tokens[0].pos.start_idx == 0
    assert tokens[0].pos.end_idx == 0
    assert tokens[0].pos.line == 1
    assert tokens[0].pos.col == 1


def test_eof_position_after_tokens():
    source = "42"
    lexer = Lexer(source)
    tokens = list(lexer.tokenize())

    assert len(tokens) == 2

    # First token '42'
    assert tokens[0].type == TokenTypes.INT
    assert tokens[0].pos.start_idx == 0
    assert tokens[0].pos.end_idx == 2

    # EOF token at index 2 (end of text)
    eof = tokens[1]
    assert eof.type == TokenTypes.EOF
    assert eof.pos.start_idx == 2
    assert eof.pos.end_idx == 2
    assert eof.pos.line == 1
    assert eof.pos.col == 3


def test_multiline_positions():
    source = "1\n+ 2"
    lexer = Lexer(source)
    tokens = list(lexer.tokenize())

    assert len(tokens) == 4

    # First token on line 1
    assert tokens[0].pos.line == 1
    assert tokens[0].pos.col == 1

    # Second token '+' on line 2, column 1
    assert tokens[1].type == TokenTypes.PLUS
    assert tokens[1].pos.line == 2
    assert tokens[1].pos.col == 1

    # Third token '2' on line 2, column 3
    assert tokens[2].type == TokenTypes.INT
    assert tokens[2].pos.line == 2
    assert tokens[2].pos.col == 3

    # EOF on line 2, col 4
    assert tokens[3].type == TokenTypes.EOF
    assert tokens[3].pos.line == 2
    assert tokens[3].pos.col == 4
