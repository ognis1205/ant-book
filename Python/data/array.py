import sys
from ctypes import py_object
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
        self._count = 0
        self._capacity = capacity
        self._data = (py_object * capacity)()

    def __len__(self):
        return self._count

    def __getitem__(self, index):
        if index < 0 or index >= self._count:
            raise IndexError('index out of bound')
        return self._data[index]

    def __setitem__(self, index, value):
        if index >= self._capacity:
            self._allocate(self._capacity * 2)
        for i in range(self._count, index + 1):
            self._data[i] = None
        self._count = max(self._count, index + 1)
        if index < 0 or index >= self._count:
            raise IndexError('index out of bound')
        self._data[index] = value

    def __str__(self):
        ret = '['
        for i in range(self._count):
            ret += str(self._data[i]) + ', '
        ret = ret.rstrip(r', ')
        ret += ']'
        return ret

    def _allocate(self, capacity):
        if capacity <= self._capacity:
            return
        self._capacity = capacity
        new_data = (py_object * capacity)()
        for i in range(self._count):
            new_data[i] = self._data[i]


INPUT = dedent('''\
0 1 2 3 4 5 6 7 8 9
''')


def main():
    with Input(INPUT) as input:
        l = list(input.readline(type=int, is_array=True))
        arr = Array()
        for i, a in enumerate(l):
            arr[i] = a
        print(f'test: {l}, {arr}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
