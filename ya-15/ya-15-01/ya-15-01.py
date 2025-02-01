P = [1, 2, 3, 4, 5, 6, 7, 10]
Q = [3, 5, 7, 8, 30]
A = list(range(1, 100))
for x in range(10 ** 4):
  f = ((Q.count(x) == 0) <= (A.count(x) == 0)) and ((P.count(x) == 1) <= (A.count(x) == 0))
  if not f:
    A.remove(x)
print(len(A), A)
