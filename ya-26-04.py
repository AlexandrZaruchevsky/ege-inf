def f(lst:list[int]):
  lst_local = [*sorted(lst)]
  m = set()
  k = 1
  for i in range(len(lst_local) - 1):
    if lst_local[i + 1] - lst_local[i] == 1:
      k += 1
    else:
      m.add(k)
      k = 1
  return max(m)


with open('data/26-04.txt', 'r') as file:
  source_list = file.readlines()
  placed_count = int(source_list[0])
  print(placed_count)
  placed_dict: dict[int, list[int]] = dict()
  for p in list(source_list[1:]):
    (key, value) = list(map(int, list(p.split())))
    pd = placed_dict.get(key)
    if pd is None:
      placed_dict.update({key: [value]})
    else:
      placed_dict.update({key: [*pd, value]})
  print(len(placed_dict))

  res = {}
  for p in list(sorted(placed_dict.keys())):
    res[p] = f(placed_dict.get(p))

  for r in res.keys():
    print(r, res[r])

file.close()
