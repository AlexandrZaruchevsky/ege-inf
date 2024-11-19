from math import sqrt

def deliteli(x):
    st:set[int] = set()
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return st

for x in range(625681, 758642):
    del_lst = list(deliteli(x))
    del_lst.sort(reverse=True)
    if len(del_lst) == 7 and len(list(filter(lambda x: True if x < 10 else False, del_lst))) == 0:
        print(del_lst[:2][::-1])