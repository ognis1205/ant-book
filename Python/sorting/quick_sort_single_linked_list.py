import io
import sys
from textwrap import dedent
from traceback import format_exc


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node({})".format(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = ""
        curr = self.head
        while curr:
            nodes += str(curr) + ","
            curr = curr.next
        nodes = nodes.strip(",")
        return "LinkedList([{}])".format(nodes)

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    @property
    def first(self):
        return self.head

    @property
    def last(self):
        if not self.head:
            return self.head
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            return curr

    def swap(self, lhs, rhs):
        tmp = lhs.data
        lhs.data = rhs.data
        rhs.data = tmp

    def partition(self, lo, hi):
        if (not lo or not hi or lo == hi):
            return
        pivot = hi.data
        prev = None
        curr = lo
        while lo != hi:
            if lo.data <= pivot:
                self.swap(curr, lo)
                prev = curr
                curr = curr.next
            lo = lo.next
        self.swap(curr, hi)
        return prev

    def sort(self, lo, hi):
        if (not lo or not hi or lo == hi):
            return
        p = self.partition(lo, hi)
        if p:
            self.sort(lo, p)
            if p.next != hi:
                self.sort(p.next.next, hi)
        else:
            self.sort(lo.next, hi)


class Input(object):
    def __init__(self, text=None):
        self._io = io.StringIO(text) if text else None

    def readline(self, parse, is_array=False):
        return list(map(parse, self._readline().split())) if is_array else parse(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()


INPUT = dedent('''\
123 3 1 424 324 5 -12309 -2 2304 -234894 2 3992 22243 23 22243 239
''')

def main():
    with Input(text=INPUT) as input_file:
        linked = LinkedList()
        for d in input_file.readline(int, is_array=True):
            linked.add(d)
        print(linked)
        linked.sort(linked.first, linked.last)
        print(linked)


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
