# Проверка, все ли цифры в числе различные
def f1(x):
  s = set(map(str, str(x)))
  return len(s) == len(str(x))


# Алгоритм вычисления
# Максимальная и минимальная цифры числа складываются.
# Остальные две цифры перемножаются.
# Полученные два числа записываются друг за другом в порядке неубывания (без разделителей).
#
def f2(x):
  lst = list(map(int, str(x)))
  mi = min(lst)
  ma = max(lst)
  s1 = mi + ma
  lst1 = list(filter(lambda x: (x != mi and x != ma), lst))
  s2 = lst1[0] * lst1[1]
  lr = sorted([s1, s2])
  return int(str(lr[0]) + str(lr[1]))


# Тест функции f1
print(f1(1123))
print(f1(1234))

# Тест функции f2
print(f2(1234))

for x in range(1000, 10000):
  if f1(x) and f2(x) > 85:
    print(x)
    break
