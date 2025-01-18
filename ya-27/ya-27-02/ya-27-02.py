import os

to_point = lambda x: (float(x.split()[0].replace(',', '.')), float(x.split()[1].replace(',', '.')))


def centroid(cluster):
  x_centr, y_centr, resm = 0, 0, 10 ** 100
  for i in range(len(cluster)):
    res = 0
    for j in range(len(cluster)):
      x1, y1 = cluster[i]
      x2, y2 = cluster[j]
      res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if res < resm:
      resm = res
      x_centr, y_centr = x1, y1
  return x_centr, y_centr


with open(os.path.abspath('.') + '/ya-27-02-b.txt', 'r') as f:
  source = list(map(to_point, f.readlines()))
  cluster1 = [x for x in source if 4 >= x[1] >= 0]
  cluster2 = [x for x in source if 7 >= x[1] >= 4]
  cluster3 = [x for x in source if x[1] >= 7]
  c1 = centroid(cluster1)
  c2 = centroid(cluster2)
  c3 = centroid(cluster3)
  print((c1[0] + c2[0] + c3[0]) / 3 * 10000, (c1[1] + c2[1] + c3[1]) / 3 * 10000)
