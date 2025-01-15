def f(x, n):
  if x >= 229 or n > 5:
    return n == 3 or n == 5
  ls = [f(x + 2, n + 1), f(x + 3, n + 1), f(x + 4, n + 1), f(x * 2, n + 1)]
  if n % 2 == 0:
    return any(ls)
  return all(ls)


def f1(x, n):
  if x >= 229 or n > 5:
    return n == 3
  ls = [f1(x + 2, n + 1), f1(x + 3, n + 1), f1(x + 4, n + 1), f1(x * 2, n + 1)]
  if n % 2 == 0:
    return any(ls)
  return all(ls)


print([s for s in range(1, 228 + 1) if f(s, 1)])
print([s for s in range(1, 228 + 1) if f1(s, 1)])
