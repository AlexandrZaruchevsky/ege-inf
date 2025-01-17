import os
from itertools import combinations

animalPoint = lambda x: (float(x.split()[0]), float(x.split()[1]))
n = 5
m = 2
with open(os.path.abspath('.') + '/' + 'ya-27-01-b.txt', 'r') as f:
# n = 3
# m = 1
# with open(os.path.abspath('.') + '/' + 'ya-27-01-a.txt', 'r') as f:
  source = list(map(animalPoint, f.readlines()))
  animalPoints = dict()
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      ls = set([x for x in source if 1 >= (i - x[0]) >= 0 and 1 >= (j - x[1]) >= 0])
      animalPoints[(i, j)] = ls
  keys = animalPoints.keys()
  ma = 0
  resm = tuple()
  for key in keys:
    ls1 = [(x, key[1]) for x in [key[0], key[0] - 1, key[0] + 1] if n >= x >= 1 and x != key[0]]
    ls2 = [(key[0], x) for x in [key[1], key[1] - 1, key[1] + 1] if n >= x >= 1 and x != key[1]]
    for k in combinations([*ls1, *ls2], r=m):
      lkeys = (key, *k)
      ls = []
      for kk in lkeys:
        ls = [*ls, *animalPoints[kk]]
      if ma < len(ls):
        ma = len(ls)
        resm = (lkeys, ls)

  ll = 0
  for p1 in resm[1]:
    x1, y1 = p1
    l = 0
    for p2 in resm[1]:
      x2, y2 = p2
      res = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
      if 0.1 >= res >= 0:
        l += 1
    if l >= 14: ll += 1
  print(resm[0], '-->', ll, len(resm[1]) -ll)

