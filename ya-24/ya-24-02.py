import os

filename = "{}/data/24-02.txt".format(os.path.dirname(__file__))

with open(filename) as file:
    source = file.read()
    flag_start = False
    str = ''
    lst = []
    i = 0
    while i < len(source):
        s = source[i]
        if s not in 'EF':
            str += s
        else:
            if len(str) > 0:
                lst.append(len(str))
            str =''
        i += 1
    print(max(lst))

file.close()