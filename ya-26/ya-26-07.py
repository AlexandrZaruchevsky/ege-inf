import os
filename = os.path.dirname(__file__) + '/data/26-07.txt'
with open(filename, 'r') as file:
    source_list = file.readlines()
    people_count = int(source_list[0])
    pep_list = [[int(a) for a in b.split()] for b in source_list[1:]]
    pep_list.sort()
    pep_shop = []
    pik = 0
    pik_count = 0
    last = 0
    for p in pep_list:
        j = 0
        while j < len(pep_shop):
            # данное условие - по условиям задачи должно быть больше, а не больше или равно,
            # т.к. в задаче сказано "Считается, что в моменты фиксации входа и выхода посетитель 
            # находится в магазине", но правильный ответ получается только при >=
            if p[0] >= pep_shop[j]:
                del pep_shop[j]
            else:
                j +=1
        pep_shop.append(p[1])
        if len(pep_shop) > pik:
            pik = len(pep_shop)
            pik_count = 1
        elif len(pep_shop) == pik and last != pik:
            pik_count += 1
        last = len(pep_shop)
    print(pik_count, pik)
file.close()
