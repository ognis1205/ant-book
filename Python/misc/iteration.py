import sys
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc


def repeat(fillvalue):
    class Infinite:
        def __init__(self, fillvalue):
            self.fillvalue = fillvalue

        def __iter__(self):
            while True:
                yield self.fillvalue

    return iter(Infinite(fillvalue))


def zip_longest(*args, fillvalue=None):
    iters = [iter(arg) for arg in args]
    num_active = len(iters)
    while True:
        ret = []
        for i, it in enumerate(iters):
            try:
                ret.append(next(it))
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iters[i] = repeat(fillvalue)
                ret.append(fillvalue)
        yield ret


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def readline(self, clean=lambda x: x, is_array=False, delimiter=r'\s+', parse=str):
        return [parse(x) for x in split(delimiter, self._readline(clean))] if is_array else parse(self._readline(clean))

    def _readline(self, clean):
        return clean(self._io.readline().strip())


INPUT = dedent('''\
1 2 3 4 5 6 7 8 9 0
a, b, c, d
[ognis 1205]
''')


def main():
    with UserInput(INPUT) as user_input:
        xs = user_input.readline(is_array=True)
        ys = user_input.readline(is_array=True, delimiter=r'\s*,\s*')
        zs = user_input.readline(is_array=True, clean=lambda x: x.rstrip(r']').lstrip(r'['))
        print(f'test: {xs}')
        print(f'test: {ys}')
        print(f'test: {zs}')

        for x, y, z in zip_longest(xs, ys, zs):
            print(f'test: {x}, {y}, {z}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
