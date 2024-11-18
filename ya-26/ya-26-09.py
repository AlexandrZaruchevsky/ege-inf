import os
filename = "{}/data/26-09.txt".format(os.path.dirname(__file__))
with open(filename) as file:
    source_list =file.readlines()
    box_count = int(source_list[0])
    box_list = [int(x) for x in source_list[1:]]
    box_list.sort(reverse=True)
    cell_list: list[list[int]] = []
    for b in box_list:
        if len(cell_list) == 0:
            cell_list.append([b])
        else:
            isAppend = False
            for i in range(len(cell_list)):
                mi = min(cell_list[i])
                if (mi - b) >= 7:
                    cell_list[i] = [*cell_list[i], b]
                    isAppend = True
                    break
            if not isAppend:
                cell_list.append([b])
    print(len(cell_list), max(list(map(lambda x: len(x), cell_list))))
file.close()