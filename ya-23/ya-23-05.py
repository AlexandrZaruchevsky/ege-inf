def f(x, c):
    if c == 4:
        ans.add(x)
        return
    f(x + 2, c + 1)
    f(x * 3, c + 1)
ans = set()
f(1, 0)
print(len(ans))
