from itertools import product

c = 0
n = 0
for s in product('АЙЛМ', repeat=5):
  c += 1
  ss = ''.join(s)
  if ss.count('М') <= 1 and ss.count('ЛЛ') == 0:
    n = c
print(n, c)
