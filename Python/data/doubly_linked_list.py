import sys
from abc import abstractmethod
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, Generic


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


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


ComparableType = TypeVar('ComparableType', bound=Comparable)


class Node(Generic[ComparableType]):
    def __init__(self, data: ComparableType):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node({self.data})'


class LinkedList(Generic[ComparableType]):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data: ComparableType):
        node = Node(data)
        if not self.head or not self.tail:
            self.head = self.tail = node
            self.head.next, self.tail.prev = self.tail, self.head
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def prepend(self, data: ComparableType):
        node = Node(data)
        if not self.head or not self.tail:
            self.head = self.tail = node
            self.head.next, self.tail.prev = self.tail, self.head
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert(self, after: ComparableType, data: ComparableType):
        curr = self.head
        while curr and curr.data != after:
            curr = curr.next
        if curr:
            prev, next = curr, curr.next
            node = Node(data)
            node.prev, node.next = prev, next
            prev.next = node
            if next:
                next.prev = node
            else:
                self.tail = node

    def delete(self, data: ComparableType):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        if curr:
            prev, next = curr.prev, curr.next
            curr.prev = curr.next = None
            if prev and next:
                prev.next = next
                next.prev = prev
            elif prev:
                self.tail = prev
                prev.next = None
            elif next:
                self.head = next
                next.prev = None
            else:
                self.head = self.tail = None

    def traverse(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.tail = self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            prev = curr
            curr = curr.prev
        self.head = prev

    def sort(self):
        self._sort(self.head, self.tail)

    def _sort(self, lo, hi):
        if not lo or not hi or lo == hi:
            return
        p = self._partition(lo, hi)
        if p != lo:
            self._sort(lo, p.prev)
        if p != hi:
            self._sort(p.next, hi)

    def _partition(self, lo, hi):
        i = j = lo
        while j != hi:
            if j.data <= hi.data:
                i.data, j.data = j.data, i.data
                i = i.next
            j = j.next
        i.data, j.data = j.data, i.data
        return i

    def __str__(self):
        return f'[{", ".join(map(lambda x: str(x.data), self.traverse()))}]'


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with Input(INPUT) as input:
        line = list(input.readline(type=int, is_array=True))
        print(f'test: {line}')

        linked = LinkedList()
        for item in line:
            linked.append(item)
        for item in line:
            linked.prepend(item)
        print(f'test: {linked}')

        linked.insert(0, 10)
        linked.insert(1, 11)
        print(f'test: {linked}, {linked.tail}')
        linked.insert(6, 12)
        print(f'test: {linked}, {linked.tail}')

        linked.delete(6)
        print(f'test: {linked}, {linked.head}, {linked.tail}')
        linked.delete(6)
        print(f'test: {linked}, {linked.head}, {linked.tail}')

        linked.reverse()
        print(f'test: {linked}, {linked.head}, {linked.tail}')

        linked.sort()
        print(f'test: {linked}, {linked.head}, {linked.tail}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
