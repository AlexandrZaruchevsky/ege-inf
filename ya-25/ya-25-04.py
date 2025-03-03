from itertools import permutations
from math import sqrt
from functools import reduce

import operator

def prosto(_x:int):
  is_prime:bool = True
  for i in range(2, int(sqrt(_x)) + 1):
    if _x % i == 0:
      is_prime = False
  return is_prime

def f(_x:int):
  st:set[int] = set()
  for i in range(2, int(sqrt(_x)) + 1):
    if _x % i == 0:
      st.add(i)
      st.add(_x // i)
  return list(filter(prosto, st))

for x in range(326782, 965325):
  d1 = f(x)
  for y in permutations(d1, r=3):
    s = reduce(operator.mul, y)
    if 326782 <= s < 965325 and max(d1) - min(d1) <= 12:
      print(x ,s, max(d1) - min(d1))
      break
