from itertools import product, permutations


def f(x):
  for i in range(len(x) - 1):
    if (int(x[i]) + int(x[i + 1])) % 2 == 0:
      return False
  return True


c = 0
sss = set()
for s in permutations('НОСОЧЕЧКИ'):
  ss = ''.join(s)
  ss = ss.replace('Н', '1').replace('С', '1').replace('Ч', '1').replace('К', '1')
  ss = ss.replace('О', '2').replace('Е', '2').replace('И', '2')
  if f(ss):
    sss.add(''.join(s))
    c += 1

print(len(sss))
