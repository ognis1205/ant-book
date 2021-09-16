"""$File: ants, $Timestamp: Wed Sep 15 17:15:52 2021
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
10
3
2 6 7
""")


def ants():
    with Input(INPUT) as input_file:
        L = input_file.readline(int)
        n = input_file.readline(int)
        x = input_file.readline(int, is_array=True)
        minimum = max(map(lambda x: min(x, L - x), x))
        maximum = max(map(lambda x: max(x, L - x), x))
        print(minimum, maximum)


if __name__ == "__main__":
   try:
      ants()
   except:
      print(format_exc(), file=sys.stderr)
