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

    def readline(self, isarray=False, delimiter=r'\s+', parse=str, clean=lambda x: x):
        if line := self._readline(clean):
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
        return None

    def _readline(self, clean):
        if line := self._io.readline():
            return clean(line)
        return None


INPUT = dedent('''\
100
''')


def main():
    with UserInput(INPUT) as user_input:
        n = user_input.readline(parse=int)
        w = len(str(n - 1))
        xs = [x for x in range(n)]
        row = 1
        while len(xs) > 0:
            hs, xs = xs[:row], xs[row:]
            if row % 2 == 0:
                hs.reverse()
            print(f'{" * ".join(map(lambda h: str(h).rjust(w), hs)).rjust(w * row + 3 * (row - 1))}')
            row += 1


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
