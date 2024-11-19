import os

filename = "{}/data/24-04.txt".format(os.path.dirname(__file__))

with open(filename) as file:
    source = file.readline()
    flag_start = False
    lst_e = []
    m = 10**10
    for i in range(len(source)):
        if source[i] == 'E':
            lst_e.append(i)
    for i in range(len(lst_e) - 239):
        m=min(m, lst_e[i + 239] - lst_e[i] + 1)
    print(m)
file.close()