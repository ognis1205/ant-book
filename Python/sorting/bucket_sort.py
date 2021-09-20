"""$File: bucket_sort, $Timestamp: Sat Sep 18 16:30:14 2021
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
9.8 0.6 10.1 1.9 3.07 3.04 5.0 8.0 4.8 7.68
""")


def bucket_sort():
    """Bucket sort.

    Bucket sort, is a sorting algorithm that works by distributing elements in a given list
    into a number of buckets. Each buckets are then sorted individually, either using a bucket
    sort or another sorting algorithm.
    """
    with Input(INPUT) as input_file:
        xs = input_file.readline(float, is_array=True)
        bs = buckets(xs)
        xs = []
        for b in bs:
            for x in b:
                xs.append(x)
        print(xs)


def buckets(arr, num_buckets=10):
    lo, hi, buckets = min(arr), max(arr), []
    width = (hi - lo) / num_buckets
    for i in range(num_buckets):
        buckets.append([])
    for a in arr:
        i = indexof(a, lo, width)
        buckets[i].append(a)
    for bucket in buckets:
        bucket.sort()
    return buckets


def indexof(x, lo, width):
    diff = (x - lo) / width - int((x - lo) / width)
    if (diff == 0 and x != lo):
        return int((x - lo) / width) - 1
    else:
        return int((x - lo) / width)


if __name__ == "__main__":
   try:
      bucket_sort()
   except:
      print(format_exc(), file=sys.stderr)
