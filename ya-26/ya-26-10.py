import os
filename = os.path.dirname(__file__) + '/data/26-10.txt'

with open(filename, 'r') as file:
    source_list = file.readlines()
    box_count = int(source_list[0])
    box_list = [int(x) for x in source_list[1:]]
    box_list.sort(reverse=True)
    mi = max(box_list) + 10
    c = 0
    for b in box_list:
        if mi - b >= 3:
            mi = b
            c += 1
    print(c, mi)
file.close()