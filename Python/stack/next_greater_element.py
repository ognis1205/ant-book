import sys
from collections import deque
from io import StringIO
from re import split
from pathlib import Path
from textwrap import dedent
from traceback import format_exc


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


INPUT = dedent('''\
5 4 3 4 5
''')


def main():
    with Path('./next_greater_element').open(mode='r') as f:
        with UserInput(f.read()) as user_input:
            items = list(user_input.readline(parse=int, is_array=True))
            print(f'test: {items}')

            ret = [0] * len(items)
            deq = deque()

            for i, item in enumerate(items):
                while len(deq) and items[deq[-1]] < items[i]:
                    ret[deq.pop()] = i + 1
                deq.append(i)

            print(f'test: {ret}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
