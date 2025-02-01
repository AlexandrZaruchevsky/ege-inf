f = open('ya-09-07.csv')
ls = []
for s in f:
  ll = list(map(int, s.split(',')))
  ss = set(ll)
  chet_count = len([x for x in ll if x % 2 != 0])
  if (len(ll) != len(ss) and chet_count != 3) or (len(ll) == len(ss) and chet_count == 3):
    ls.append(ll)
print(len(ls))
