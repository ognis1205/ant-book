"""$File: external_sort, $Timestamp: Tue Sep 21 03:19:50 2021
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
   input = raw_input
except NameError:
   pass

import io
import os
import sys
from copy import deepcopy
from math import sqrt
from itertools import (
    combinations,
    combinations_with_replacement,
    islice,
    permutations
)
from textwrap import dedent
from traceback import format_exc


class Input(object):
    def __init__(self, text=None):
        self._io = io.StringIO(text) if text else sys.stdin

    def readline(self, parser=str, is_array=False):
        asarray = lambda line: self._asarray(parser, line)
        return asarray(self._readline()) if is_array else parser(self._readline())

    def readlines(self, n, parser=str, is_array=False):
        asarray = lambda line: self._asarray(parser, line)
        return map(asarray, self._readlines(n)) if is_array else map(parser, self._readlines(n))

    def _readline(self):
        return self._io.readline().strip()

    def _readlines(self, n):
        return [x.strip() for x in islice(self._io, n)]

    def _asarray(self, parser, line):
        return map(parser, line.split())

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()


def array(n, generate=lambda i: 0):
    return [deepcopy(generate(i)) for i in range(n)]


INPUT = dedent("""\
6
7
8
9
2
5
3
4
1
""")


def external_sort():
    with Input(INPUT) as input_file:
        ms = mergers(input_file, 2, io.StringIO)
        loop(sys.stdout, ms)


def loop(output_file, mergers):
    stack = [int(merger.readline()) for merger in mergers]
    while stack:
        c = min(stack)
        output_file.write("{}\n".format(c))
        i = stack.index(c)
        n = mergers[i].readline()
        if n:
            stack[i] = int(n)
        else:
            del stack[i]
            mergers[i].close()
            del mergers[i]


def mergers(input_file, run_length, opener=open):
    ms = []
    while True:
        xs = input_file.readlines(run_length, int)
        if not len(xs):
            break;
        xs.sort()
        m = opener()
        for x in xs:
            m.write("{}\n".format(x))
        m.seek(0)
        ms.append(m)
    return ms


if __name__ == "__main__":
   try:
      external_sort()
   except:
      print(format_exc(), file=sys.stderr)
