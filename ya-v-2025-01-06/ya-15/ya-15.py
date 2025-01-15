#
left = -100000
right = 100000
B = {-42, -10, -8, 2, 16}
C = {-10, -4, 2, 15, 23}
A = {a for a in range(left, right)}
ls = list()
for x in range(left, right):
  if (not(x in A) or x in B) or x in C:
    ls.append(x)
print(sum([ x for x in ls if x>=0]))
