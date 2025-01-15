li = list(map(int, open('ya-17.txt').readlines()))
mi3 = sorted(list(map(int ,list(filter(lambda x : len(x) == 3, list(map(str, li)))))))[1] ** 2

lst = list()

# вариант 1
for i in range(len(li) - 1):
  s = li[i] + li[i+1]
  if s <  mi3:
    lst.append(s)

# вариант 1
lss = [(li[i] + li[i+1]) for i in range(len(li)-1) if (li[i] + li[i+1]) < mi3]

print(len(lst), max(lst))
print(len(lss), max(lss))
