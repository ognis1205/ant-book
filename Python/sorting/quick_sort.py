import sys
from abc import abstractmethod
from io import StringIO
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, MutableSequence


class Input:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else None

    def readline(self, parse=str, is_array=False):
        return map(parse, self._readline().split()) if is_array else parse(self._readline())
        

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()


class Comparable(Protocol):
    @abstractmethod
    def __lt__():
        pass


ComparableType = TypeVar('ComparableType', bound=Comparable)


def partition(seq: MutableSequence[ComparableType], start: int, end: int) -> int:
    assert 0 <= start < len(seq) and 0 <= end < len(seq) and start <= end
    i = start
    p = seq[end]
    for j in range(start, end):
        if seq[j] < p:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1
    seq[i], seq[end] = seq[end], seq[i]
    return i


def qsort(seq: MutableSequence[ComparableType], start: int, end: int) -> None:
    if start >= end:
        return
    p = partition(seq, start, end)
    qsort(seq, start, p - 1)
    qsort(seq, p + 1, end)


INPUT = '''\
5 3 -10 2 10
'''

def main():
    with Input(INPUT) as input:
        seq = list(input.readline(parse=int, is_array=True))
        qsort(seq, 0, 4)
        print('result: ', seq)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(format_exc(), file=sys.stderr)
