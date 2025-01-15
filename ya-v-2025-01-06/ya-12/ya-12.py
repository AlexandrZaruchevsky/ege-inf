# Вариант 1
def f(ss:str):
  while '111' in ss or '66' in ss:
    ss = ss.replace('6666', '1', 1)
    ss = ss.replace('111', '3', 1)
    ss = ss.replace('66', '6', 1)
  return len(list(filter(lambda x : x == 3, list(map(int, ss))))) >= 5

for n in range(3, 10000):
  s='1'
  for i in range(n):
    s += '6'
  if f(s):
    print(n)
    break

# Вариант 2
for n in range(3, 10000):
  s='1'
  for i in range(n):
    s += '6'
  while '111' in s or '66' in s:
    s = s.replace('6666', '1', 1)
    s = s.replace('111', '3', 1)
    s = s.replace('66', '6', 1)
  if len(list(filter(lambda x : x == 3, list(map(int, s))))) >= 5:
    print(n)
    break
