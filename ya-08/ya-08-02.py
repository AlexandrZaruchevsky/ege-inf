from itertools import product

c = 0
flag = False
for s in product('ВГОРСТ', repeat=6):
  c += 1
  if ''.join(s) == 'СГОВОР':
    flag = True
  if flag:
    ss = ''.join(s)
    ss = ss.replace('В', '*').replace('Г', '*').replace('С', '*').replace('Р', '*').replace('Т', '*')
    if ss.count('**') == 0:
      print(c, ''.join(s))
      break
