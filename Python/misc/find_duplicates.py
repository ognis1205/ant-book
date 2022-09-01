import sys
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def readline(self, parse=str, delimiter=r'\s+', isarray=False, clean= lambda x: x):
        if line := self._readline(clean):
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
        return None

    def _readline(self, clean):
        if line := self._io.readline():
            return clean(line.strip())
        return None


INPUT = dedent('''\
0, 4, 3, 2, 7, 8, 2, 3, 1
''')


def main():
    with UserInput(INPUT) as user_input:
        xs = user_input.readline(
            isarray=True,
            delimiter=r'\s*,\s*',
            parse=int
        )
        l = len(xs)
        for i in range(l):
            x = xs[i] % l
            xs[x] += l
        for i in range(l):
            print(f'{xs[i] % l}') if xs[i] >= l * 2 else ...


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
