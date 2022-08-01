import sys
from io import StringIO
from dataclasses import dataclass, field
from re import split
from textwrap import dedent
from traceback import format_exc
from typing import (
    Any,
    Generic,
    TypeVar,
    Sequence,
    Tuple,
)


NodeType = TypeVar('NodeType', bound='Node')

@dataclass(frozen=True, eq=True)
class Node(Generic[NodeType]):
    value: Any
    children: Sequence[NodeType] = field(default_factory=list, compare=False)


def balance(node: Node) -> Tuple[Sequence[Node], Sequence[Node]]:
    card = lambda n: sum(card(c) for c in n.children) + 1
    lhs = sorted(node.children, key=lambda c: card(c))
    rhs = []
    while lhs and sum([card(n) for n in lhs]) > sum([card(n) for n in rhs]):
        rhs.append(lhs.pop())
    return lhs, rhs


def htree(node: Node, indent='', prev='topbottom'):
    name = str(node.value)
    up, down = balance(node)

    for child in up:
        htree(
            child,
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
        r = ' '

    print(f'{indent}{l}{name}{r}')

    for child in down:
        htree(
            child,
            f'{indent}{" " if "bottom" in prev else "|"}{" " * len(name)}',
            'bottom' if down.index(child) == len(down) - 1 else '')


class UserInput:
    def __init__(self, text=None):
        self._io = StringIO(text) if text else sys.stdin

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if hasattr(self._io, 'close'):
            self._io.close()

    def readline(self, parse=str, is_array=False, delimiter=r'\s+', clean=lambda x: x):
        if line := self._readline(clean):
            return [parse(x) for x in split(delimiter, line)] if is_array else parse(line)
        return None

    def _readline(self, clean):
        if line := self._io.readline():
            return clean(line.strip())
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
                parse=int,
                is_array=True,
                delimiter=r'\s*,\s*',
                clean=lambda x: x.lstrip('[').rstrip(']')):
            p = memo.setdefault(edge[0], Node(edge[0]))
            c = memo.setdefault(edge[1], Node(edge[1]))
            p.children.append(c)
            children.add(edge[1])
        roots = set(memo.keys()) - children
        for root in roots:
            htree(memo[root])


if __name__ == '__main__':
    try:
        main()
    except:
        print(format_exc(), file=sys.stderr)
