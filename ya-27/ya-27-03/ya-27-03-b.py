import os


def centroid(cluster: list):
  x_centr, y_centr, minim = 0, 0, 10 ** 100
  for i in range(len(cluster)):
    res = 0
    for j in range(len(cluster)):
      x1, y1 = cluster[i]
      x2, y2 = cluster[j]
      res += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if res < minim:
      minim = res
      x_centr, y_centr = cluster[i]
  return x_centr, y_centr


with open(os.path.abspath('.') + '/ya-27-03-b.csv', 'r') as f:
  points = f.readlines()
  clusters = [[] for _ in range(5)]
  for p in points:
    x, y = map(float, p.replace(',', '.').split())

    if 1 > x > -3 and 2 > y > -3:
      clusters[0].append((x,y))
    if 7 > x > 3 and 1 > y > -3:
      clusters[1].append((x, y))
    if 3 > x > -1 and 6 > y > 2:
      clusters[2].append((x, y))
    if 7 > x > 3 and 5 > y > 1:
      clusters[3].append((x, y))
    if 8 > x > 3 and 8 > y > 5:
      clusters[4].append((x, y))
  maxP = max([len(cl) for cl in clusters])
  clstrs = list(filter(lambda x: len(x) != maxP, clusters))
  cluster_count = len(clstrs)
  sumx, sumy = 0, 0
  for c in clstrs:
    x, y = centroid(c)
    sumx += x
    sumy += y
  print(sumx / cluster_count * 10000, sumy / cluster_count * 10000)
