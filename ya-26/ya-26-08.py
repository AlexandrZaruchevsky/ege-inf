import os
filename = "{}/data/26-08.txt".format(os.path.dirname(__file__))
with open(filename, 'r') as file:
    source_list = file.readlines()
    tovar_count = int(source_list[0])
    tovar_list = list(map(int, source_list[1:]))
    tovar_list.sort()
    tovar_p = [*tovar_list[3 * tovar_count // 4:], *list(map(lambda x: x // 2, tovar_list[3 * tovar_count // 4:]))]
    tovar_m = [*tovar_list[tovar_count // 4:], *list(map(lambda x: x // 2, tovar_list[:tovar_count // 4]))]
    print(sum(tovar_p), sum(tovar_m))
file.close()