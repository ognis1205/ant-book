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

    def readline(self, parse=str, is_array=False, delimiter=r'\s+'):
        return map(parse, split(delimiter, self._readline())) if is_array else parse(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()


ComparableType = TypeVar('ComparableType', bound='Comparable')


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other):
        pass


NodeType = TypeVar('Node', bound='Node')


@dataclass
class Node(Generic[ComparableType]):
    data: ComparableType
    next: Optional[NodeType] = None


class LinkedList(Generic[ComparableType]):
    def __init__(self):
        self.head = None

    @property
    def tail(self):
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        return curr

    def prepend(self, data: ComparableType):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data: ComparableType):
        if not self.head:
            self.head = Node(data)
        else:
            self.tail.next = Node(data)

    def delete(self, condition):
        try:
            prev, found = next(self._find(condition))
            if prev:
                prev.next = found.next
            elif found:
                self.head = found.next
        except StopIteration:
            return

    def insert(self, after, data):
        try:
            _, found = next(self._find(lambda x: x == after))
            tmp = found.next
            node = Node(data)
            found.next, node.next = node, tmp
        except StopIteration:
            pass

    def find(self, condition):
        try:
            _, found = next(self._find(condition))
            return found.data if found else None
        except StopIteration:
            return None

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            tmp = curr.next
            prev, curr.next = curr, prev
            curr = tmp
        self.head = prev

    def sort(self):
        self._sort(self.head, self.tail)

    def _sort(self, start, end):
        if not start or not end or start == end:
            return
        prev = self._partition(start, end)
        if prev:
            self._sort(start, prev)
            if prev.next != end:
                self._sort(prev.next.next, end)
        else:
            self._sort(start.next, end)

    def _partition(self, start, end):
        p = None
        i = j = start
        while j != end:
            if j.data <= end.data:
                i.data, j.data = j.data, i.data
                p, i = i, i.next
            j = j.next
        i.data, j.data = j.data, i.data
        return p

    def _find(self, condition):
        for p, n in self._traverse():
            if condition(n.data):
                yield p, n

    def _traverse(self):
        prev, curr = None, self.head
        while curr:
            yield prev, curr
            prev, curr = curr, curr.next

    def __iter__(self):
        return map(lambda n: n[1].data, self._traverse())

    def __str__(self):
        return f'[{", ".join([str(n) for n in self])}]'


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with UserInput(text=INPUT) as user_input:
        seq = list(user_input.readline(parse=int, is_array=True))
        linked_list = LinkedList()
        for i in seq:
            linked_list.append(i)
        print(f'test: {linked_list}')

        linked_list.delete(lambda x: x == 1)
        print(f'test: {linked_list}')

        linked_list.reverse()
        print(f'test: {linked_list}')

        linked_list.insert(2, 11)
        print(f'test: {linked_list}')

        linked_list.sort()
        print(f'test: {linked_list}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
