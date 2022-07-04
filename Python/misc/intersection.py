import sys
from abc import abstractmethod
from dataclasses import dataclass
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, Generic, Optional


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()

    def readline(self, is_array=False, parse=str, delimiter=r'\s+'):
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


NodeType = TypeVar('NodeType', bound='Node')

@dataclass
class Node(Generic[ComparableType, NodeType]):
    data: ComparableType
    next: Optional[NodeType] = None


class LinkedList(Generic[ComparableType]):
    def __init__(self):
        self.head = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        return f'[{", ".join(map(lambda n: str(n.data), self))}]'

    def append(self, data: ComparableType):
        if not self.head:
            self.head = Node(data)
        else:
            self.tail.next = Node(data)

    @property
    def tail(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr


INPUT = dedent('''\
1 2 3 4 6
2 4 6 8
''')

def main():
    with UserInput(INPUT) as user_input:
        line = list(user_input.readline(is_array=True, parse=int))
        lhs = LinkedList[int]()
        for i in line:
            lhs.append(i)
        line = list(user_input.readline(is_array=True, parse=int))
        rhs = LinkedList[int]()
        for i in line:
            rhs.append(i)
        print(f'test: {lhs}')
        print(f'test: {rhs}')

        ret = LinkedList[int]()
        l = lhs.head
        r = rhs.head
        while l and r:
            if l.data == r.data:
                ret.append(l.data)
                l, r = l.next, r.next
            elif l.data < r.data:
                l = l.next
            elif r.data < l.data:
                r = r.next
        print(f'test: {ret}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
