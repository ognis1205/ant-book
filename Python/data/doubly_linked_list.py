import sys
from abc import abstractmethod
from dataclasses import dataclass
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, Generic, Optional, Callable


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


class Comparable:
    @abstractmethod
    def __le__(self, other):
        pass


NodeType = TypeVar('NodeType', bound='Node')


@dataclass
class Node(Generic[ComparableType, NodeType]):
    data: ComparableType
    prev: Optional[NodeType] = None
    next: Optional[NodeType] = None


class LinkedList(Generic[ComparableType]):
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        return map(lambda n: n.data, self._traverse())

    def __str__(self):
        return f'[{", ".join(map(str, self))}]'

    def prepend(self, data: ComparableType):
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            node: Node[ComparableType, Node] = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, data: ComparableType):
        if not self.head:
            self.head = self.tail = Node(data)
        else:
            node: Node[ComparableType, Node] = Node(data)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insert(self, after: ComparableType, data: ComparableType):
        try:
            found: Node[ComparableType, Node] = next(self._find(lambda x: x == after))
            node: Node[ComparableType, Node] = Node(data)
            if found.next:
                node.prev, node.next = found, found.next
                found.next = node
            else:
                node.prev, found.next = found, node
                self.tail = node
        except StopIteration:
            return

    def delete(self, data: ComparableType):
        try:
            found: Node[ComparableType, Node] = next(self._find(lambda x: x == data))
            p, n = found.prev, found.next
            if p:
                p.next = n
            else:
                self.head = n
            if n:
                n.prev = p
            else:
                self.tail = p
        except StopIteration:
            return

    def find(self, cond: Callable[[ComparableType], bool]):
        return map(lambda n: n.data, self._find(cond))

    def sort(self):
        self._sort(self.head, self.tail)

    def _sort(
            self,
            start: Optional[Node[ComparableType, Node]],
            end: Optional[Node[ComparableType, Node]]):
        if not start or not end or start == end:
            return
        p = self._partition(start, end)
        if p != start:
            self._sort(start, p.prev)
        if p != end:
            self._sort(p.next, end)

    def _partition(
            self,
            start: Optional[Node[ComparableType, Node]],
            end: Optional[Node[ComparableType, Node]]):
        i = j = start
        while i and j and end and j != end:
            if j.data <= end.data:
                i.data, j.data = j.data, i.data
                i = i.next
            j = j.next
        if i and j:
            i.data, j.data = j.data, i.data
        return i

    def _find(self, cond: Callable[[ComparableType], bool]):
        curr = self.head
        while curr:
            if cond(curr.data):
                yield curr
            curr = curr.next

    def _traverse(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next


INPUT = dedent('''\
1 0 2 9 3 8 4 7 5 6
''')


def main():
    with UserInput(INPUT) as user_input:
        seq = list(user_input.readline(is_array=True, parse=int))
        linked_list = LinkedList[int]()
        for i in seq:
            linked_list.append(i)
        print(f'test: {linked_list}')

        found = list(linked_list.find(lambda data: data % 2 == 0))
        print(f'test: {found}')

        linked_list.delete(2)
        print(f'test: {linked_list}')

        linked_list.delete(1)
        print(f'test: {linked_list}, {linked_list.head.data}')

        linked_list.delete(6)
        print(f'test: {linked_list}, {linked_list.tail.data}')

        linked_list.insert(3, 11)
        print(f'test: {linked_list}')

        linked_list.insert(5, 22)
        print(f'test: {linked_list}, {linked_list.tail.data}')

        linked_list.sort()
        print(f'test: {linked_list}')


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(format_exc(), file=sys.stderr)
