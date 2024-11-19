import os

filename = "{}/data/24-01.txt".format(os.path.dirname(__file__))

raznochet = lambda x, y: True if (x % 2 - y % 2) != 0 else False

with open(filename, 'r') as file:
    source = file.read()
    print(len(source))
    flag_start = False
    str=''
    lst = []
    i = 0
    while i < len(source):
        s = source[i]
        if s in '0123456789':
            if not flag_start:
                flag_start = True
                str += s
            else:
                flag_start = False
                str += s
                if raznochet(int(str[0]), int(str[-1])):
                    lst.append(len(str))
                str = ''
                i -= 1
        else:
            if flag_start:
                str += s
        i += 1
    print(max(lst))
file.close()