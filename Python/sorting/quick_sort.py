"""$File: quick_sort, $Timestamp: Thu Sep 16 17:17:13 2021
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
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from textwrap import dedent
from traceback import format_exc


class Input(object):
    def __init__(self, text=None):
        self._io = io.StringIO(text) if text else None

    def readline(self, parser=str, is_array=False):
        return map(parser, self._readline().split()) if is_array else parser(self._readline())

    def _readline(self):
        return self._io.readline().strip() if self._io else input().strip()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        if self._io:
            self._io.close()


def array(n, generate=lambda i: 0):
    return [deepcopy(generate(i)) for i in range(n)]


INPUT = dedent("""\
123 3 1 424 324 5 -12309 -2 2304 -234894 2 3992 22243 23 22243 239
""")


def quick_sort():
    """Quick sorting.

    Quick sort is an divide-and-conquer algorithm. It works by selecting a pivot element
    from a given list and partitioning the other element into two sub list, according
    to whether they are less or greater then the pivot. The sub arrays are then recursively
    sorted.
    """
    with Input(INPUT) as input_file:
        x = input_file.readline(int, is_array=True)
        sort(x, 0, len(x) - 1)
        print(x)


def sort(x, l, r):
    if l < r:
        p = partition(x, l, r)
        sort(x, l, p - 1)
        sort(x, p + 1, r)


def partition(x, l, r):
    i, p = l, x[r]
    for j in range(l, r + 1):
        if x[j] < p:
            x[i], x[j] = x[j], x[i]
            i += 1
    x[i], x[r] = x[r], x[i]
    return i


if __name__ == "__main__":
   try:
      quick_sort()
   except:
      print(format_exc(), file=sys.stderr)
