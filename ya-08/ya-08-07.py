from itertools import product

c = 0
n = 0
for s in product(sorted([s for s in 'ПРОБНИК']), repeat=6):
  c += 1
  if s.count('О')==3 and len(set(s)) == 4:
    n = c
print(n)