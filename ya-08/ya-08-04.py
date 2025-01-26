from itertools import product

c = 0
ls = []
for s in product('БДЕЖИКНТЮ', repeat=6):
  if ''.join(s) == 'БЮДЖЕТ': break
  c += 1
  ss = ''.join(s)
  ss = ss.replace('Б','1').replace('Д','1').replace('Ж','1').replace('К','1')
  ss = ss.replace('Н', '1').replace('Т', '1')
  ss = ss.replace('Е', '2').replace('И', '2').replace('Ю', '2')
  if ss.count('11') == 0 and ss.count('22') == 0:
    ls.append(c)
print(sum(ls))


