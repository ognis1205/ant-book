import sys
from abc import abstractmethod
from dataclasses import dataclass
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, Generic, Optional, Callable


ComparableType = TypeVar('ComparableType', bound='Comparable')

class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass


NodeType = TypeVar('NodeType', bound='Node')

@dataclass
class Node(Generic[ComparableType, NodeType]):
    data: ComparableType
    next: Optional[NodeType] = None


class LinkedList(Generic[ComparableType]):
    def __init__(self):
        self.tail = None

    def __iter__(self):
        return map(lambda n: n.data, self._traverse())

    def __str__(self):
        return f'[{", ".join(map(lambda n: str(n[1].data), self._traverse(once=True)))}]'

    def append(self, data: ComparableType):
        if not self.tail:
            self.tail = Node(data)
            self.tail.next = self.tail
        else:
            node: Node[ComparableType, Node] = Node(data)
            tmp = self.tail.next
            self.tail.next = node
            node.next = tmp
            self.tail = node

    def insert(self, after: ComparableType, data: ComparableType):
        try:
            _, found = next(self._find(lambda x: x == after))
            node: Node[ComparableType, Node] = Node(data)
            tmp: Node[ComparableType, Node] = found.next
            found.next = node
            node.next = tmp
            if found == self.tail:
                self.tail = node
        except StopIteration:
            return

    def delete(self, data: ComparableType):
        try:
            prev, found = next(self._find(lambda x: x == data))
            if prev == found:
                self.tail = None
            else:
                prev.next = found.next
                if found == self.tail:
                    self.tail = prev
        except StopIteration:
            return

    def sort(self):
        self._sort(self.tail.next, self.tail)

    def _sort(self, start, end):
        if not start or not end or start == end:
            return
        p = self._partition(start, end)
        if p:
            self._sort(start, p)
            if p.next != end:
                self._sort(p.next.next, end)
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

    def find(self, cond: Callable[[ComparableType], bool]):
        return map(lambda n: n[1].data, self._find(cond, once=True))

    def _find(self, cond: Callable[[ComparableType], bool], once=False):
        return filter(lambda n: cond(n[1].data), self._traverse(once))

    def _traverse(self, once=False):
        if self.tail:
            prev = self.tail
            head = curr = self.tail.next
            while curr:
                yield prev, curr
                prev = curr
                curr = curr.next
                if once and curr == head:
                    break


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


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with UserInput(text=INPUT) as user_input:
        line = list(user_input.readline(is_array=True, parse=int))
        linked_list = LinkedList[int]()
        for i in line:
            linked_list.append(i)
        print(f'test: {linked_list}')

        for d in linked_list.find(lambda x: x % 2 == 0):
            print(f'test: {d}')

        linked_list.insert(2, 11)
        print(f'test: {linked_list}')
        linked_list.insert(6, 12)
        print(f'test: {linked_list}')

        linked_list.delete(2)
        print(f'test: {linked_list}')
        linked_list.delete(12)
        print(f'test: {linked_list}')

        linked_list.sort()
        print(f'test: {linked_list}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
