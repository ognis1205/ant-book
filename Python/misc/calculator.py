import sys
import enum
from abc import abstractmethod
from dataclasses import dataclass, field
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import (
    Optional,
    Callable,
    Any,
    Iterator,
    TypeVar,
    Generic,
)


class TokenType(enum.Enum):
    NUM = enum.auto()
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()
    LPR = enum.auto()
    RPR = enum.auto()


@dataclass
class Token:
    token_type: TokenType
    value: Optional[float] = field(default=None)


class Lexer:
    SPACES = ' \t'

    DIGITS = '1234567890'

    def __init__(self, raw_string: str):
        self._raw_string = iter(raw_string)
        self.advance()

    @property
    def has_next(self):
        return self.next_char is not None

    def tokens(self) -> Iterator[Token]:
        while self.has_next:
            if self.next_char == '.' or self.next_char in Lexer.DIGITS:
                yield Token(TokenType.NUM, self.consume_number())
            elif self.next_char == '+':
                yield Token(TokenType.ADD)
                self.advance()
            elif self.next_char == '-':
                yield Token(TokenType.SUB)
                self.advance()
            elif self.next_char == '*':
                yield Token(TokenType.MUL)
                self.advance()
            elif self.next_char == '/':
                yield Token(TokenType.DIV)
                self.advance()
            elif self.next_char == '(':
                yield Token(TokenType.LPR)
                self.advance()
            elif self.next_char == ')':
                yield Token(TokenType.RPR)
                self.advance()
            elif self.next_char in Lexer.SPACES:
                self.advance()
            else:
                raise Exception(f'invalid character: {self.next_char}')

    def advance(self) -> str:
        try:
            self.next_char = next(self._raw_string)
        except StopIteration:
            self.next_char = None

    def consume_number(self) -> float:
        acc, num_decimal_point = self.next_char, 1 if self.next_char == '.' else 0
        self.advance()
        while self.next_char and (self.next_char == '.' or self.next_char in Lexer.DIGITS):
            if self.next_char == '.':
                num_decimal_point += 1
                if num_decimal_point > 1:
                    break
            acc += self.next_char
            self.advance()
        return float(acc)


AST = TypeVar('AST', bound='AbstractSyntaxTree')

class AbstractSyntaxTree:
    @abstractmethod
    def __repr__(self):
        pass


@dataclass
class Number(AbstractSyntaxTree):
    value: float

    def __repr__(self):
        return f'{self.value}'


@dataclass
class Add(AbstractSyntaxTree, Generic[AST]):
    lhs: AST
    rhs: AST

    def __repr__(self):
        return f'{repr(self.lhs)} + {repr(self.rhs)}'


@dataclass
class Sub(AbstractSyntaxTree, Generic[AST]):
    lhs: AST
    rhs: AST

    def __repr__(self):
        return f'{repr(self.lhs)} - {repr(self.rhs)}'


@dataclass
class Mul(AbstractSyntaxTree, Generic[AST]):
    lhs: AST
    rhs: AST

    def __repr__(self):
        return f'{repr(self.lhs)} * {repr(self.rhs)}'


@dataclass
class Div(AbstractSyntaxTree, Generic[AST]):
    lhs: AST
    rhs: AST

    def __repr__(self):
        return f'{repr(self.lhs)} / {repr(self.rhs)}'


class Parser:
    def __init__(self, raw_string):
        self._tokens = Lexer(raw_string).tokens()
        self.advance()

    @property
    def has_next(self):
        return self.next_token is not None

    @property
    def is_additive(self):
        return self.next_token.token_type in (TokenType.ADD, TokenType.SUB)

    @property
    def is_cumulative(self):
        return self.next_token.token_type in (TokenType.MUL, TokenType.DIV)

    def AST(self) -> AST:
        if not self.next_token:
            return None
        ast = self.expr()
        if self.next_token:
            raise Exception(f'illegal expression: {self.next_token}')
        return ast

    def expr(self) -> AST:
        ast = self.term()
        while self.has_next and self.is_additive:
            if self.next_token.token_type is TokenType.ADD:
                self.advance()
                ast = Add(ast, self.term())
            elif self.next_token.token_type is TokenType.SUB:
                self.advance()
                ast = Sub(ast, self.term())
        return ast

    def term(self) -> AST:
        ast = self.factor()
        while self.has_next and self.is_cumulative:
            if self.next_token.token_type == TokenType.MUL:
                self.advance()
                ast = Mul(ast, self.factor())
            elif self.next_token.token_type == TokenType.DIV:
                self.advance()
                ast = Div(ast, self.factor())
        return ast

    def factor(self) -> AST:
        if self.next_token.token_type == TokenType.LPR:
            self.advance()
            expr = self.expr()
            if not self.next_token or self.next_token.token_type != TokenType.RPR:
                raise Exception(f'invalid expression: {self.next_token}')
            self.advance()
            return Number(eval(repr(expr)))
        elif self.next_token.token_type == TokenType.NUM:
            value = self.next_token.value
            self.advance()
            return Number(value)
        elif self.next_token.token_type == TokenType.ADD:
            self.advance()
            return Number(eval(repr(self.factor())))
        elif self.next_token.token_type == TokenType.SUB:
            self.advance()
            return Number(- 1.0 * eval(repr(self.factor())))
        raise Exception(f'invalid expression: {self.next_token}')

    def advance(self):
        try:
            self.next_token = next(self._tokens)
        except StopIteration:
            self.next_token = None


Clean = Callable[[str], str]

Parse = Callable[[str], Any]

class UserInput:
    def __init__(self, text: Optional[str] = None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def _readline(self, clean: Clean) -> Optional[str]:
        if line := self._io.readline().strip():
            return clean(line)
        return None

    def readline(
            self,
            isarray: bool = False,
            delimiter: str = r'\s+',
            clean: Clean = lambda x: x,
            parse: Parse = str) -> Optional[str]:
        if line := self._readline(clean):
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
        return None


INPUT = dedent('''\
(1 + 2 * (3.5 - 9.0)) / 2
''')


def main():
    with UserInput(INPUT) as user_input:
        while line := user_input.readline():
            print(line)
            print(f'result: {eval(repr(Parser(line).AST()))}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
