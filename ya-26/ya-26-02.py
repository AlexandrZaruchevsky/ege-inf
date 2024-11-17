with open('data/26-02.txt') as file:
  source = file.readlines()
  file_size_list = sorted(list(map(int, source[1:])))
  disk_size = int(source[0].split()[0])
  user_count = int(source[0].split()[1])
  s = []
  k = 0
  for i in file_size_list:
    s.append(i)
    k += 1
    if sum(s) > disk_size:
      sss = [*s[::-1][1:]]
      print(disk_size - (sum(sss)-max(sss)))
      print(sorted(set(file_size_list))[::-1])
      print(k - 1)
      break
file.close()
