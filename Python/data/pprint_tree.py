import sys
from abc import abstractmethod
from dataclasses import dataclass, field
from io import StringIO
from itertools import zip_longest, chain, repeat
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import Protocol, TypeVar, MutableSequence, List


def separate_by_card(node):
    card = lambda n: sum(card(c) for c in n.children) + 1
    lhs = sorted([c for c in node.children], key=lambda n: card(n))
    rhs = []
    while lhs and sum([card(n) for n in rhs]) < sum([card(n) for n in lhs]):
        rhs.append(lhs.pop())
    return lhs, rhs


def pptree_horizontally(node, separate, indent='', prev='topbottom'):
    name = str(node)
    up, down = separate(node)

    for child in up:     
        pptree_horizontally(
            child,
            separate,
            f'{indent}{" " if "top" in prev else "|"}{" " * len(name)}',
            'top' if up.index(child) == 0 else '')

    if prev == 'top':
        l = '┌'
    elif prev == 'bottom':
        l = '└'
    elif prev == 'topbottom':
        l = ' '
    else:
        l = '├'

    if up:
        r = '┤'
    elif down:
        r = '┐'
    else:
        r = ''

    print(f'{indent}{l}{name}{r}')

    for child in down:
        pptree_horizontally(
            child,
            separate,
            f'{indent}{" " if "bottom" in prev else "│"}{" " * len(name)}',
            'bottom' if down.index(child) is len(down) - 1 else '')


def pptree_vertically(node):
    pass


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

    def __str__(self):
        return str(self.data)


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
[2000,4000]
[1000,2000]
[3000,6000]
[1000,3000]
[2000,5000]
[4000,7000]
[4000,8000]
[4000,9000]
[4000,1100]
[4000,1200]
[3000,1300]
[3000,1400]
[7000,1500]
[7000,1600]
[7000,1700]
[7000,1800]
[7000,1900]
[7000,1110]
[3000,1120]
[3000,1130]
[1000,1140]
[1000,1150]
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
        pptree_horizontally(p, separate_by_card)


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
