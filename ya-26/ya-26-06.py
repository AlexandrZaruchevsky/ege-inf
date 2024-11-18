import os
filename = os.path.dirname(__file__) + '/data/26-06.txt'
with open(filename, 'r') as file:
    source = file.readlines()
    lot_dict: dict[int, list[int]] = dict()
    for s in source[1:]:
        (lot, uch, stavka) = list(map(int, s.split()))
        zl = lot_dict.get(lot)
        if zl is None:
            lot_dict.update({lot: [stavka]})
        else:
            lot_dict.update({lot: [*zl, stavka]})
    lot_prod = []
    for key in lot_dict.keys():
        zl = sorted(lot_dict[key])
        if len(zl) >= 2:
            lot_prod.append(zl[len(zl)-2])
    print(len(lot_prod), sum(lot_prod))
file.close()