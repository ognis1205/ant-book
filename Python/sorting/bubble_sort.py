"""$File: bubble_sort, $Timestamp: Thu Sep 16 16:06:57 2021
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


def bubble_sort():
    """Bubble sorting.

    Bubble sorting is a simple algorithm that repeatedly steps through a given array,
    compares adjacent elements and swaps them if they are in wrong order.

    Average time complexity: O(n^2)
    Average space complexity: O(1), in-place
    """
    with Input(INPUT) as input_file:
        xs = input_file.readline(int, is_array=True)
        loop(xs)
        print(xs)


def loop(arr):
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i, j in zip(range(len(arr))[:], range(len(arr))[1:]):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                is_swapped = True


if __name__ == "__main__":
   try:
      bubble_sort()
   except:
      print(format_exc(), file=sys.stderr)
