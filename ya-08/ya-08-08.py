from itertools import product

i = 0
c = 0
for s in product(sorted('АПРЕЛЬ', reverse=True), repeat = 6):
  i += 1
  if i == 387:
    break
  if s[5] == 'Ь':
    c += 1
print(c)