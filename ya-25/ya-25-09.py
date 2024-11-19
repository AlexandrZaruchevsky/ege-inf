from math import sqrt

def deliteli(x):
    st:set[int] = set()
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return list(st)


c = 0
for x in range(700000, 10 ** 10):
    del_lst = (list(filter(lambda x: True if x != 7 and str(x).endswith('7') else False, deliteli(x))))
    if len(del_lst) > 0:
        c += 1
        print(x, min(del_lst))
    
    if c >= 5: 
        break