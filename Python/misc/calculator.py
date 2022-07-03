import sys
from enum import Enum
from traceback import format_exc


class TokenType(Enum):
    NUM = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    LPR = 6
    RPR = 7

    def __str__(self):
        return self.name


class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f'Token({str(self.token_type)}, {self.value})'


class Lexer:
    WHITESPACES = ' \n\t'

    DIGITS = '0123456789'

    def __init__(self, text):
        self._text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.next_char = next(self._text)
        except StopIteration:
            self.next_char = None

    @property
    def has_next(self):
        return self.next_char is not None

    @property
    def has_whitespace(self):
        return self.next_char in Lexer.WHITESPACES

    @property
    def has_numeric(self):
        return self.next_char == '.' or self.next_char in Lexer.DIGITS

    @property
    def has_plus(self):
        return self.next_char == '+'

    @property
    def has_minus(self):
        return self.next_char == '-'

    @property
    def has_multiply(self):
        return self.next_char == '*'

    @property
    def has_division(self):
        return self.next_char == '/'

    @property
    def has_left_paren(self):
        return self.next_char == '('

    @property
    def has_right_paren(self):
        return self.next_char == ')'

    def tokens(self):
        while self.has_next:
            if self.has_whitespace:
                self.advance()
            elif self.has_numeric:
                yield self.parse_number()
            elif self.has_plus:
                self.advance()
                yield Token(TokenType.ADD)
            elif self.has_minus:
                self.advance()
                yield Token(TokenType.SUB)
            elif self.has_multiply:
                self.advance()
                yield Token(TokenType.MUL)
            elif self.has_division:
                self.advance()
                yield Token(TokenType.DIV)
            elif self.has_left_paren:
                self.advance()
                yield Token(TokenType.LPR)
            elif self.has_right_paren:
                self.advance()
                yield Token(TokenType.RPR)
            else:
                raise Exception(f'illegal character "{self.next_char}"')

    def parse_number(self):
        value = self.next_char
        num_decimal_point = 0
        self.advance()

        while self.has_next and self.has_numeric:
            if self.next_char == '.':
                num_decimal_point += 1
                if num_decimal_point > 1:
                    break
            value += self.next_char
            self.advance()

        if value.startswith('.'):
            value = '0' + value
        if value.endswith('.'):
            value = value + '0'

        return Token(TokenType.NUM, float(value))


def lex(raw_string):
    lexer = Lexer(raw_string)
    for lexeme in lexer.tokens():
        print(lexeme)


def main():
    lex('1 + (2 / 3) + -.1234')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
