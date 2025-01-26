from itertools import product

count = 0
for c in product('0123456789ABCD', repeat=5):
  cc = ''.join(c)
  cc = cc.replace('1', '*').replace('3', '*').replace('5', '*').replace('7', '*').replace('9', '*')
  cc = cc.replace('A', '-').replace('B', '-').replace('C', '-').replace('D', '-')
  if cc[0] != '0' and  cc.count('*-') == 0 and cc.count('-*') == 0:
    print(''.join(c))
    count += 1
print(count)
