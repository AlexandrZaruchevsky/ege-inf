from itertools import product

c=0
for s in product('012345', repeat=6):
  ss = ''.join(s).replace('1', '*').replace('3', '*').replace('5', '*')
  if ss[0]!='0' and ss.count('2') == 1 and ss.count('*2') == 0 and ss.count('2*') == 0:
    c += 1
print(c)