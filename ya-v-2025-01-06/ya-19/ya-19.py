def f(x, n):
  if x >= 229 or n > 3:
    return n == 3
  ls = [f(x + 2, n + 1), f(x + 3, n + 1), f(x + 4, n + 1), f(x * 2, n + 1)]
  if n % 2 == 0:
    return any(ls)
  return all(ls)


lst = [s for s in range(1, 228 + 1) if f(s, 1)]

print(min(lst))
