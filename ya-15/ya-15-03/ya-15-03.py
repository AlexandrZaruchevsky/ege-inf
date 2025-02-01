def con(x: int, y: int):
  x_b, y_b = bin(x)[2:], bin(y)[2:]
  maxl = len(x_b) if len(x_b) >= len(y_b) else len(y_b)
  x_b, y_b = x_b.zfill(maxl), y_b.zfill(maxl)
  s = ''
  for i in range(maxl):
    s += '1' if x_b[i] == y_b[i] == '1' else '0'
  return int(s, 2)


for a in range(1, 10 ** 6):
  c = 0
  for x in range(15, 31):
    f = (con(x, 29) == 0) or ((con(x, 11) == 0) <= (not (con(x, a) == 0)))
    if f: c += 1
  if c == 16:
    print(a)
    break
