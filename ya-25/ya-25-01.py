import re
pattern = re.compile(r'^[13579]136\d*1$')
li11071 = [x for x in range(11071, 10 ** 10, 11071) if pattern.match(str(x)) is not None and int(str(x)[4:-1]) % 2 == 0]
li11071.sort(reverse=True)
for x in li11071[:5][::-1]:
  print(x, x // 11071)