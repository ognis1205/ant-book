import sys
from abc import abstractmethod
from dataclasses import dataclass
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import MutableSequence, Protocol, TypeVar


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


ComparableType = TypeVar('ComparableType', bound='Comparable')

class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


def qsorted(seq: MutableSequence[ComparableType]):
    _qsorted(seq, 0, len(seq) - 1)


def _qsorted(seq: MutableSequence[ComparableType], start: int, end: int):
    if not 0 <= start < len(seq) or not 0 <= end < len(seq) or start >= end:
        return
    p = _partition(seq, start, end)
    _qsorted(seq, start, p - 1)
    _qsorted(seq, p + 1, end)


def _partition(seq: MutableSequence[ComparableType], start: int, end: int):
    i = j = start
    while j < end:
        if seq[j] <= seq[end]:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
        j += 1
    seq[i], seq[j] = seq[j], seq[i]
    return i


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6 11 -22 33 -44 
''')


def main():
    with UserInput(INPUT) as user_input:
        line = list(user_input.readline(is_array=True, parse=int))
        print(f'test: {line}')

        qsorted(line)
        print(f'test: {line}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
