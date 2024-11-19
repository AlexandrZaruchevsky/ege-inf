import re
pattern = re.compile(r'^3\d12\d14\d*5$')
lst1917 = [x for x in range(1917, 10 ** 10, 1917) if pattern.match(str(x)) is not None]
for x in lst1917:
    print(x, x // 1917)