f = open('ya-09-05.csv')
c = 0
for s in f:
  ls = list(map(int, s.split(',')))
  dic = dict()
  for x in ls:
    dic[x] = [x] if dic.get(x) is None else [*dic.get(x), x]
  lv = sorted(dic.values(), key=len, reverse=True)
  if len(lv) == 5 and  len(lv[0]) == 2:
    if sum([*lv[0], *lv[1]]) / 4 < sum(ls)/len(ls):
      c += 1
print(c)