import sys
from dataclasses import dataclass
from enum import Enum
from traceback import format_exc
from typing import Optional


class TokenType(Enum):
    NUM = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    LPR = 6
    RPR = 7


@dataclass
class Token:
    token_type: TokenType
    value: Optional[float] = None


@dataclass
class Number:
    value: float

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Add:
    lhs: any
    rhs: any

    def __repr__(self):
        return f'{repr(self.lhs)} + {repr(self.rhs)}'


@dataclass
class Subtratc:
    lhs: any
    rhs: any

    def __repr__(self):
        return f'{repr(self.lhs)} - {repr(self.rhs)}'


@dataclass
class Multiply:
    lhs: any
    rhs: any

    def __repr__(self):
        return f'{repr(self.lhs)} * {repr(self.rhs)}'


@dataclass
class Divide:
    lhs: any
    rhs: any

    def __repr__(self):
        return f'{repr(self.lhs)} / {repr(self.rhs)}'


@dataclass
class Plus:
    child: any

    def __repr__(self):
        return f'+{repr(self.child)}'


@dataclass
class Minus:
    child: any

    def __repr__(self):
        return f'-{repr(self.child)}'


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


class Parser:
    def __init__(self, tokens):
        self._tokens = tokens
        self.advance()

    def advance(self):
        try:
            self.next_token = next(self._tokens)
        except StopIteration:
            self.next_token = None

    @property
    def has_next(self):
        return self.next_token is not None

    @property
    def has_additive(self):
        return self.next_token.token_type in (TokenType.ADD, TokenType.SUB)

    @property
    def has_multiplicative(self):
        return self.next_token.token_type in (TokenType.MUL, TokenType.DIV)

    def parse(self):
        if not self.has_next:
            return None
        tree = self.expr()
        if self.has_next:
            raise Exception('invalid syntax')
        return tree

    def expr(self):
        tree = self.term()
        while self.has_next and self.has_additive:
            if self.next_token.token_type == TokenType.ADD:
                self.advance()
                tree = Add(tree, self.term())
            elif self.next_token.token_type == TokenType.SUB:
                sels.advance()
                tree = Subtract(tree, self.term())
        return tree

    def term(self):
        tree = self.factor()
        while self.has_next and self.has_multiplicative:
            if self.next_token.token_type == TokenType.MUL:
                self.advance()
                tree = Multiply(tree, self.factor())
            elif self.next_token.token_type == TokenType.DIV:
                self.advance()
                tree = Divide(tree, self.factor())
        return tree

    def factor(self):
        token = self.next_token
        if token.token_type == TokenType.LPR:
            self.advance()
            tree = self.expr()
            if self.next_token.token_type != TokenType.RPR:
                raise Exception('invalid syntax')
            self.advance()
            return Number(eval(repr(tree)))
        elif token.token_type == TokenType.NUM:
            self.advance()
            return Number(token.value)
        elif token.token_type == TokenType.ADD:
            self.advance()
            return Plus(self.factor())
        elif token.token_type == TokenType.SUB:
            self.advance()
            return Minus(self.factor())
        raise Exception('invalid syntax')


def interpret(raw_string):
    lexer = Lexer(raw_string)
    parser = Parser(lexer.tokens())
    tree = parser.parse()
    print(eval(repr(tree)))


def main():
    while line := input('enter :'):
        interpret(line)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
