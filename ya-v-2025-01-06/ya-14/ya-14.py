alpha = '0123456789ABCD'
ls = []
for y in alpha:
  for x in alpha:
    f = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
    if f % 9 == 0:
      ls.append(f // 9)
print(max(ls))