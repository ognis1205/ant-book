import sys
#import numpy as np
from collections import deque
from io import StringIO
from re import split
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

    def readline(self, parse=str, is_array=False, delimiter=r'\s+'):
        return map(parse, split(delimiter, self._readline())) if is_array else parse(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()


INPUT = dedent('''\
5 4 3 4 5
''')


def main():
    with UserInput(INPUT) as user_input:
        items = list(user_input.readline(is_array=True, parse=int))
        print(f'test: {items}')

        l = _left_indices(items)
        r = _right_indices(items)
        p = list(map(lambda x: x[0] * x[1], zip(l, r)))
        print(f'test: {l}')
        print(f'test: {r}')
        print(f'test: {max(p)}')


def _left_indices(seq):
    ret = [0] * len(seq)
    deq = deque()

    for i in reversed(range(len(seq))):
        while len(deq) and seq[deq[-1]] < seq[i]:
            ret[deq.pop()] = i + 1
        deq.append(i)

    return ret


def _right_indices(seq):
    ret = [0] * len(seq)
    deq = deque()

    for i in range(len(seq)):
        while len(deq) and seq[deq[-1]] < seq[i]:
            ret[deq.pop()] = i + 1
        deq.append(i)

    return ret


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
