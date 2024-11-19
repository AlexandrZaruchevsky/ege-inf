import os

filename = "{}/data/24-05.txt".format(os.path.dirname(__file__))

with open(filename) as file:
    source = file.readline()
    flag_start = False
    lst = []
    m = 0
    for i in range(len(source) - 5):
        if source[i: i + 5] =='AHAHA':
            lst.append(i)
    for i in range(len(lst) -1):
        # отнимаем длину AHAHA (-5) и прибавляем в начало HAHA (+4), а в конец AHAH (+4)
        m = max(m, lst[i+1] - lst[i] - 5 + 4 + 4)
    print(m)

file.close()