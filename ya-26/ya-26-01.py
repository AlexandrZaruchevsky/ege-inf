def f(x: int, d: dict[int, int]):
  if x == 0:
    return d
  for key in list(d.keys())[::-1]:
    if key <= x:
      w = d.get(key)
      if w == key:
        d.pop(key)
      else:
        d.update({key: w - int(key)})
      return f(x - key, d)
  return dict()


with open('data/26-01.txt', 'r') as file:
  weights = sorted(list(map(int, file.readlines()[1:])))
  weight_dict: dict[int, int] = dict()
  for i in weights:
    wd = weight_dict.get(i)
    if wd is None:
      weight_dict.update({i: i})
    else:
      weight_dict.update({i: wd + i})
  v = 0
  for i in range(1, sum(list(weight_dict.keys())[::-1]) + 1):
    if len(f(i, weight_dict.copy())) == 0:
      v = i - 1
      print(i)
      break
  ddd = f(v, weight_dict.copy())
  print(sum([ddd.get(i) // i for i in list(ddd.keys())]))
file.close()
