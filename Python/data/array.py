import sys
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc


class Input:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else None

    def readline(self, type=str, is_array=False, delimiter=r'\s+'):
        return map(type, split(delimiter, self._readline())) if is_array else type(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()


class Array:
    def __init__(self, capacity=1024):
        self.capacity = capacity


INPUT = dedent('''\
0 1 2 3 4 5 6 7 8 9
''')


def main():
    with Input(INPUT) as input:
        l = list(input.readline(type=int, is_array=True))
        print(f'test: {l}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
