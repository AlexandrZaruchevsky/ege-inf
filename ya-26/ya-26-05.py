import os
filename = os.path.dirname(__file__) + '/data/26-05.txt'

with open(filename) as file:
    source = file.readlines()
    cell_count = int(source[0])
    pass_count = int(source[1])
    pass_list = [[int(a) for a in x.split()] for x in source[2:]]
    pass_list.sort()
    cell_list = [0] * cell_count
    pass_last = 0
    cell_last = 0
    for p in pass_list:
        for i in range(len(cell_list)):
            if p[0] > cell_list[i]:
                cell_list[i] = p[1]
                pass_last += 1
                cell_last = i + 1
                break
    print(pass_last, cell_last)
        
file.close()