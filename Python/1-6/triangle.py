"""$File: triangle, $Timestamp: Thu Sep 16 14:58:36 2021
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
5
2 3 4 5 10
""")


def triangle():
    with Input(INPUT) as input_file:
        n = input_file.readline(int)
        a = sorted(input_file.readline(int, is_array=True), reverse=True)
        for one, two, three in zip(a[:], a[1:], a[2:]):
            if one < two + three:
                print(one + two + three)
                return
        print(0)


if __name__ == "__main__":
   try:
      triangle()
   except:
      print(format_exc(), file=sys.stderr)
