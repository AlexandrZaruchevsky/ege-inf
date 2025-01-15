# ГИПЕРБОЛА
from itertools import product

glas = 'ИЕОА'
soglas = 'ГПРБЛ'

def f(ss):
  for j in range(1, len(ss) - 1):
    if ss[j] in glas and (ss[j - 1] in soglas and ss[j + 1] in soglas):
      return False
  return True

c = 0
for s in product("ГИПЕРБОЛА", repeat=6):
  if s[0] not in glas and s[-1] not in glas:
    if f(s):
      c += 1
print(c)

print((2**39)/2)

274877906944
274877906944
274877906944