def deliteli(x):
    st:set[int] = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return list(st)

c = 0
for x in range(424242 + 1, 10**10):
    del_lst = deliteli(x)
    m = min(del_lst) + max(del_lst) if len(del_lst)>0 else 0
    if m % 2024 == 42:
        c += 1
        print(x, m)
    if c >= 8:
        break

