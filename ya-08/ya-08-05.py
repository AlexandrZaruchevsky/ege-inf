from itertools import permutations
c=0
for s in permutations('КОБУРА'):
  ss= ''.join(s)
  ss = ss.replace('К', '1').replace('Б', '1').replace('Р', '1')
  ss = ss.replace('О', '2').replace('У', '2').replace('А', '2')
  if ss == '121212' or ss == '212121':
    c += 1

print(c)
