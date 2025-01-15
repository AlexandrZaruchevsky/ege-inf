def f(x, n):
  if x >= 229 or n > 4:
    return n == 4
  ls = [f(x + 2, n + 1), f(x + 3, n + 1), f(x + 4, n + 1), f(x * 2, n + 1)]
  if n % 2 == 1:
    return any(ls)
  return all(ls)


lst = [s for s in range(1, 228 + 1) if f(s, 1)]

print(lst)
