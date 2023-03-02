import sys
from io import StringIO
from traceback import format_exc
from re import split
from textwrap import dedent


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def readline(self, parse=str, clean=lambda x: x.strip(), delimiter=r'\s+', isarray=False):
        line = self._readline(clean)
        if line:
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
        else:
            return None

    def _readline(self, clean):
        line = self._io.readline()
        if line:
            return clean(line)
        else:
            return None


INPUT = dedent('''\
3 2
1 5 3
3 1
5 7
''')


def main():
    with UserInput(INPUT) as user_input:
        line = user_input.readline(isarray=True, parse=int)
        print(line)
        line = user_input.readline(isarray=True, parse=int)
        print(line)
        line = user_input.readline(isarray=True, parse=int)
        print(line)
        line = user_input.readline(isarray=True, parse=int)
        print(line)
        line = user_input.readline(isarray=True, parse=int)
        print(line)


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
