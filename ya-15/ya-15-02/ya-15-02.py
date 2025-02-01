for a in range(300):
  c = 0
  for x in range(10 ** 5):
    f = (x ^ a != 2) and not ((x ^ 9 != 5) <= (x ^ 27 != 7))
    if not f:
      c += 1
  if c == 10 ** 5:
    print(a)
    break
