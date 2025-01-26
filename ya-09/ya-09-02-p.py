f = open('ya-09-02.csv')
c = 0
for s in f:
  ls = list(map(int, s.split(';')))
  sd = dict()
  for x in ls:
    sd[x] = [x] if sd.get(x) is None else [*sd.get(x), x]
    lsv = sorted(sd.values(), key=len, reverse=True)
    if len(lsv) == 4 and len(lsv[0]) == 3:
      if sum(lsv[0]) ** 2 > (sum(ls) - sum(lsv[0])) ** 2:
        c += 1
print(c)
