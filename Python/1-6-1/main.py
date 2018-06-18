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
   n = get_line_as(int)
   a = get_line_as(int, in_array=True)
   assert(n == len(a))

   acc = 0
   for i in range(n):
      for j in range(i+1, n):
         for k in range(j+1, n):
            e = sorted([a[i], a[j], a[k]])
            if e[2] <= e[0] + e[1]:
               acc = max(acc, e[0] + e[1] + e[2])
   print(acc)


if __name__ == "__main__":
   try:
      main()
   except:
      print(format_exc(), file=sys.stderr)
