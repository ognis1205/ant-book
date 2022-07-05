import sys
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import TypeVar, Generic


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()

    def readline(self, is_array=False, parse=str, delimiter=r'\s+'):
        return map(parse, split(delimiter, self._readline())) if is_array else parse(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()


class Deque:
    def __init__(self):
        self._data = []

    def __iter__(self):
        return self._data

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f'[{", ".join(map(str, self._data))}]'

    def push(self, data):
        self._data.append(data)

    def pop(self, is_stack=True):
        try:
            return self._data.pop(-1 if is_stack else 0)
        except IndexError:
            return None

    def peek(self, is_stack=True):
        try:
            return self._data[-1] if is_stack else self._data[0]
        except IndexError:
            return None

    def insert(self, index, data):
        self._data.insert(index, data)


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with UserInput(INPUT) as user_input:
        items = list(user_input.readline(is_array=True, parse=int))
        deque = Deque()
        for item in items:
            deque.push(item)
        print(f'test: {deque}')

        while len(deque):
            print(f'test: {deque.pop()}')
        print(f'test: {deque}')

        for item in items:
            deque.push(item)
        print(f'test: {deque}')

        while len(deque):
            print(f'test: {deque.pop(is_stack=False)}')
        print(f'test: {deque}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
