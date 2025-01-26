f = open('ya-09-04.csv')
c = 0
for s in f:
  ls = list(map(int, s.split(',')))
  ls.sort(reverse=True)
  if all([x > 10 for x in ls]) and ls[0] ** 3 >= (ls[1] * ls[2] * ls[3]) * 2:
    c += 1
print(c)
