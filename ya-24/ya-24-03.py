import os

filename = "{}/data/24-03.txt".format(os.path.dirname(__file__))

with open(filename) as file:
    source = file.read()
    flag_start = False
    str = ''
    lst = []
    i = 0
    while i < len(source):
        s = source[i]
        if s == 'E':
            str += s
            if not flag_start:
                flag_start = True
            else:
                flag_start = False
                if len(str) > 0:
                    lst.append(len(str))
                str =''
                i -= 1
        else:
            if s in 'ND' and flag_start:
                str += s
            else:
                flag_start = False
                str = ''
        i += 1
    print(max(lst))
file.close()