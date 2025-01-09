def f(x, y, n, h, s):
  if x + y <= 42 or n >= 3:
    return n == 3
  lf00 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
  lf11 = [f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
  lf12 = [f(x - 4, y, n + 1, 1, 1), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
  lf21 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y // 3, n + 1, 2, 2)]
  lf22 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1)]
  if n == 1:
    return all(lf00)
  if h == 1:
    return any(lf11) if s == 1 else any(lf12)
  else:
    return any(lf21) if s == 1 else any(lf22)

for s in range(1, 1000):
  if f(50, s, 1, 0, 0):
    print(s)
    break