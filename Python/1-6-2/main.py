from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
   input = raw_input
except NameError:
   pass

import os
import sys
from copy import deepcopy
from math import sqrt
from itertools import permutations
from itertools import combinations
from traceback import format_exc


def get_line():
   return input()

def get_line_as(parse, in_array=False):
   return map(parse, get_line().split()) if in_array else map(parse, get_line().split())[0]

def array(n, value=0):
   return [deepcopy(value) for i in range(n)]

def main():
   L = get_line_as(int)
   n = get_line_as(int)
   x = get_line_as(int, in_array=True)
   assert(n == len(x))

   acc_min, acc_max = (0, 0)
   for i in range(n):
      l_min, l_max = sorted([L - x[i], x[i]])
      acc_min = max(acc_min, l_min)
      acc_max = max(acc_max, l_max)
   print('min = {}'.format(acc_min))
   print('max = {}'.format(acc_max))


if __name__ == "__main__":
   try:
      main()
   except:
      print(format_exc(), file=sys.stderr)
