chet = lambda x : sum([ x for x in  list(map(int, str(x))) if x % 2 == 0 ]) ** 2

def sub_pow_3(x):
  lst = list(map(int, str(x)))
  return (max(lst) - min(lst)) ** 3

for x in range(1000, 10000):
  lst = sorted([ chet(x), sub_pow_3(x) ])
  s = str(lst[0]) + str(lst[1])
  if s == '4343':
    print(x)
    break