import sys
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc


class Reader:
    def __init__(self, file=None):
        self._file = file if file else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._file, 'close'):
            self._file.close()

    def readline(
            self,
            isarray=False,
            parse=str,
            delimiter=r'\s+',
            clean=lambda x: x.strip()
    ):
        line = self._readline(clean)
        if line:
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
        else:
            return None

    def _readline(self, clean):
        line = self._file.readline()
        if line:
            return clean(line)
        else:
            return None


INPUT = dedent('''\
input
''')


def main():
    with Reader(file=StringIO(INPUT)) as r:
        print(f'{r.readline()}')
        print(f'{r.readline()}')
        print(f'{r.readline()}')

    with open('test.txt', 'r') as f, Reader(file=f) as r:
        print(f'{r.readline()}')
        print(f'{r.readline()}')
        print(f'{r.readline()}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
