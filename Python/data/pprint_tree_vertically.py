import sys
import enum
from dataclasses import dataclass, field
from io import StringIO
from itertools import zip_longest, chain, repeat
from re import split, finditer
from textwrap import dedent
from traceback import format_exc
from typing import (
    Any,
    TypeVar,
    Generic,
    Sequence,
)


NodeType = TypeVar('NodeType', bound='Node')

@dataclass
class Node(Generic[NodeType]):
    value: Any
    children: Sequence[NodeType] = field(default_factory=list, compare=False)

    def __str__(self):
        return f'{self.value}'


def concat(*columns, joiners=()):
    widths = tuple(max(map(len, c), default=0) for c in columns)
    return list(
        joiner.join(
            x.center(width)
            for x, width in zip(row, widths)
        )
        for row, joiner in zip(zip_longest(*columns, fillvalue=''), chain(joiners, repeat(' ')))
    )


def get_str_width(column):
    if not column or not column[0]:
        return (None, None)
    indices = [(m.start(), m.end()) for m in finditer(r'\S+', column[0])]
    return (indices[0][0], indices[-1][1] - 1) if indices else (None, None)


def get_column_width(column):
    if not column:
        return 0
    return max(map(len, column), default=0)


def draw(column, box_drawing):
    l_padding = ' ' if box_drawing == '┌' else '─'
    r_padding = ' ' if box_drawing == '┐' else '─'
    w = get_column_width(column)
    l, r = get_str_width(column)
    if l is not None and r is not None:
        l = (l + r) // 2
        r = w - l - 1
    elif w > 0:
        l = w // 2
        r = w - l - 1
    else:
        l = r = 0
    return [f'{l_padding * l}{box_drawing}{r_padding * r}'] + column


def bifurcate(*columns):
    return concat(*list(map(lambda c: draw(c, '┬'), columns)), joiners=('─',))


def left(*columns):
    head, *tail = columns
    return concat(draw(head, '┌'), bifurcate(*tail), joiners=('─',))


def right(*columns):
    *head, tail = columns
    return concat(bifurcate(*head), draw(tail, '┐'), joiners=('─',))


def branches(lhs, rhs):
    return concat(lhs, rhs, joiners=(('┴' if rhs else '┘') if lhs else '└',))


def balance(node):
    card = lambda n: sum(card(c) for c in n.children) + 1
    lhs = sorted([c for c in node.children], key=lambda n: card(n))
    rhs = []
    while lhs and sum(card(n) for n in lhs) > sum(card(n) for n in rhs):
        rhs.append(lhs.pop())
    return lhs, rhs


def vtree(node):
    name = str(node)
    lhs, rhs = balance(node)
    lhs = left(*[vtree(n) for n in lhs]) if lhs else []
    rhs = right(*[vtree(n) for n in rhs]) if rhs else []
    lw = get_column_width(lhs)
    rw = get_column_width(rhs)
    name = f'{" " * lw}{name}{" " * rw}'
#    return concat([name], branches(lhs, rhs))
    return [name] + branches(lhs, rhs)


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def _readline(self, clean):
        if line := self._io.readline().strip():
            return clean(line)
        return None

    def readline(self, parse=str, isarray=False, delimiter=r'\s+', clean=lambda x: x):
        if line := self._readline(clean):
            return [parse(x) for x in split(delimiter, line)] if isarray else parse(line)
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
[1130,1160]
[1160,1170]
''')


def main():
    with UserInput(INPUT) as user_input:
        memo = dict()
        children = set()
        while edge := user_input.readline(
                isarray=True,
                parse=int,
                clean=lambda x: x.lstrip('[').rstrip(']'),
                delimiter=r'\s*,\s*'):
            p = memo.setdefault(edge[0], Node(edge[0]))
            c = memo.setdefault(edge[1], Node(edge[1]))
            p.children.append(c)
            children.add(c.value)
        for root in set(memo.keys()) - children:
            tree = vtree(memo[root])
            print('\n'.join(tree))


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
