import re
from math import sqrt

pattern = re.compile(r'^34\d8\d*9$')

def is_prosto(x):
    is_prime = True
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
    return is_prime

def deliteli(x):
    st:set[int] = set()
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            st.add(i)
            st.add(x // i)
    return st

lst = [x for x in range(10 ** 7) if pattern.match(str(x)) is not None]

for x in lst:
    prosto_deliteli = list(filter(is_prosto, deliteli(x)))
    if len(prosto_deliteli) > 4:
        print(x, '->', max(prosto_deliteli))