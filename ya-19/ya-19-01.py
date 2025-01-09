def f(x, y, n, v):
  if x + y <= 42 or n >= 3:
    return n == 3
  lf0 = [f(x - 4, y, n + 1, 1), f(x // 3, y, n + 1, 2), f(x, y - 4, n + 1, 3), f(x, y // 3, n + 1, 4)]
  lf1 = [f(x // 3, y, n + 1, 2), f(x, y - 4, n + 1, 3), f(x, y // 3, n + 1, 4)]
  lf2 = [f(x - 4, y, n + 1, 1), f(x, y - 4, n + 1, 3), f(x, y // 3, n + 1, 4)]
  lf3 = [f(x - 4, y, n + 1, 1), f(x // 3, y, n + 1, 2), f(x, y // 3, n + 1, 4)]
  lf4 = [f(x - 4, y, n + 1, 1), f(x // 3, y, n + 1, 2), f(x, y - 4, n + 1, 3)]
  if n == 1: return all(lf0)
  if n % 2 == 0:
    if v == 1: return any(lf1)
    elif v == 2: return any(lf2)
    elif v == 3: return any(lf3)
    else: return any(lf4)
  if v == 1: return all(lf1)
  elif v == 2: return all(lf2)
  elif v == 3: return all(lf3)
  else: return all(lf4)


for s in range(1, 1000):
  if f(50, s, 1, 0):
    print(s)
    break



# def f(x, y, n, h, v):
#   if x + y <= 42 or n >= 3:
#     return n == 3
#   lf00 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
#   lf11 = [f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
#   lf12 = [f(x - 4, y, n + 1, 1, 1), f(x, y - 4, n + 1, 2, 1), f(x, y // 3, n + 1, 2, 2)]
#   lf21 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y // 3, n + 1, 2, 2)]
#   lf22 = [f(x - 4, y, n + 1, 1, 1), f(x // 3, y, n + 1, 1, 2), f(x, y - 4, n + 1, 2, 1)]
#   if n == 1:
#     return all(lf00)
#   if n % 2 == 0:
#     if h == 1:
#       return any(lf11) if v == 1 else any(lf12)
#     else:
#       return any(lf21) if v == 1 else any(lf22)
#   if h == 1:
#     return all(lf11) if v == 1 else all(lf12)
#   else:
#     return all(lf21) if v == 1 else all(lf22)
#
#
# for s in range(1, 1000):
#   if f(50, s, 1, 0, 0):
#     print(s)
#     break

