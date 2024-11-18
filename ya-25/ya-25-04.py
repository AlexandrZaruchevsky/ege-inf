from itertools import permutations
from math import sqrt
from functools import lru_cache, reduce

import operator

@lru_cache
def prosto(x):
  is_prime:bool = True
  for i in range(2, int(sqrt(x))+1):
    if x % i == 0:
      is_prime = False
  return is_prime

@lru_cache
def f(x:int):
  st:set[int] = set()
  for i in range(2, int(sqrt(x)) + 1):
    if x % i == 0:
      st.add(i)
      st.add(x // i)
  return list(filter(prosto, st))

for x in range(326782, 965325):
  d1 = f(x)
  for y in permutations(d1, r=3):
    s = reduce(operator.mul, y)
    if 326782 <= s < 965325 and max(d1) - min(d1) <= 12:
      print(x ,s, max(d1) - min(d1))
      break
