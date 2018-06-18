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
   m = get_line_as(int)
   k = get_line_as(int, in_array=True)

   assert(len(k) == n)
   s = sorted([k[i] + k[j] for i in range(n) for j in range(n) if i <= j])

   def search(t):
      l, r = (0, len(s)-1)
      while r - l >= 1:
         i = (l + r) // 2
         if s[i] == t:
            return True
         elif s[i] > t:
            r = i
         else:
            l = i + 1
      return False

   print(search(m))


if __name__ == "__main__":
   try:
      main()
   except:
      print(format_exc(), file=sys.stderr)
