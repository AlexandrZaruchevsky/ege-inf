from itertools import product
c=0
for s in product('012345', repeat=7):
  if s[0]!='0':
    ss = ''.join(s).replace('0','*').replace('4','*')
    if ss.count('2') == 1 and ss.count('2*')==0 and ss.count('*2')==0:
      c += 1
print(c)