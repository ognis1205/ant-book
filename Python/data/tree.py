import sys
from abc import abstractmethod
from dataclasses import dataclass, field
from io import StringIO
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, MutableSequence, List


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other):
        pass


ComparableType = TypeVar('ComparableType', bound='Comparable')

NodeType = TypeVar('NodeType', bound='Node')


@dataclass
class Node:
    data: ComparableType
    children: List[NodeType] = field(default_factory=list)


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def readline(self, parse=str, clean=lambda x: x.strip(), is_array=False, delimiter=r'\s+'):
        if line := self._readline(clean):
            return list(map(parse, split(delimiter, line))) if is_array else parse(line)
        else:
            return None

    def _readline(self, clean):
        if line := self._io.readline():
            return clean(line.strip())
        else:
            return None


INPUT = dedent('''\
[2,4]
[1,2]
[3,6]
[1,3]
[2,5]
''')


def tree(node):
    pass


def main():
    with UserInput(INPUT) as user_input:
        nodes = dict()
        children = set()
        while line := user_input.readline(
                parse=int,
                is_array=True,
                delimiter=r'\s*,\s*',
                clean=lambda x: x.lstrip('[').rstrip(']')):
            p = nodes.setdefault(line[0], Node(line[0]))
            c = nodes.setdefault(line[1], Node(line[1]))
            p.children.append(c)
            children.add(c.data)
        p = nodes[next(iter(set(nodes.keys()) - children))]
        print(f'test: {p}')


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
