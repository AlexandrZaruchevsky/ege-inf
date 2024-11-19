from math import sqrt

def deliteli(x):
    st:set[int] = set()
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return list(st)

for x in range(333555, 777999 + 1):
    del_lst = list(filter(lambda x: True if len(str(x)) == 2 else False, deliteli(x)))
    if len(del_lst) == 35:
        print(x, min(del_lst), max(del_lst))
