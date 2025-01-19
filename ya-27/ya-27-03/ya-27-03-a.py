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


with open(os.path.abspath('.') + '/ya-27-03-a.csv', 'r') as f:
  points = f.readlines()
  cluster1 = []
  cluster2 = []
  cluster3 = []
  for p in points:
    x, y = map(float, p.replace(',', '.').split())
    if y > 5.5:
      cluster1.append((x, y))
    if 5.5 > y > 2.5:
      cluster2.append((x, y))
    if y < 2.5:
      cluster3.append((x, y))
  maxP = max([len(cluster1), len(cluster2), len(cluster3)])
  clusters = list(filter(lambda x: len(x) != maxP, [cluster1, cluster2, cluster3]))
  cluster_count = len(clusters)
  sumx, sumy = 0, 0
  for c in clusters:
    x, y = centroid(c)
    sumx += x
    sumy += y
  print(sumx / cluster_count * 10000, sumy / cluster_count * 10000)
