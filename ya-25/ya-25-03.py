

import re
pattern = re.compile(r'^1\d2157\d*4$')
lst = [x for x in range(2024, 10 ** 10, 2024) if pattern.match(str(x)) is not None]
for x in lst:
  print(x, x // 2024)