import sys
from abc import abstractmethod
from io import StringIO
from itertools import islice
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, Generic, TypeVar, Optional, Callable


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
    def __init__(self, data: Optional[ComparableType] = None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'Node({str(self.data)})'


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
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def find(self, condition: Callable[[ComparableType], bool]):
        return filter(lambda n: condition(n.data), self.traverse())

    def insert(self, after: ComparableType, data: ComparableType):
        try:
            after = next(self.find(lambda x: x == after))
        except StopIteration:
            return
        node = Node(data)
        node.next = after.next
        after.next = node

    def delete(self, data: ComparableType):
        prev = curr = None
        curr = self.head
        while curr and curr.data != data:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
            curr.next = None

    def traverse(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

    def sort(self):
        self._sort(self.head, self.tail)

    def _sort(self, lo, hi):
        if (not lo or not hi or lo == hi):
            return
        p = self._partition(lo, hi)
        if p:
            self._sort(lo, p)
            if p.next != hi:
                self._sort(p.next.next, hi)
        else:
            self._sort(lo.next, hi)

    def _partition(self, lo, hi):
        p = None
        i = j = lo
        while j != hi:
            if j.data <= hi.data:
                i.data, j.data = j.data, i.data
                p = i
                i = i.next
            j = j.next
        i.data, j.data = j.data, i.data
        return p

    def to_list(self):
        return list(map(lambda n: n.data, self.traverse()))

    def __str__(self):
        ret = self.to_list()
        return f'[{", ".join(map(str, ret))}]'


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with Input(INPUT) as input:
        items = list(input.readline(type=int, is_array=True))

        linked_list = LinkedList()
        for item in items:
            linked_list.prepend(item)
        print(f'test: {linked_list}')

        for i in linked_list.find(lambda x: x % 2 == 0):
            print(i)

        linked_list.insert(3, 10)
        linked_list.insert(3, 9)
        print(f'test: {linked_list}')

        linked_list.sort()
        print(f'test: {linked_list}')

        linked_list.reverse()
        print(f'test: {linked_list}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
