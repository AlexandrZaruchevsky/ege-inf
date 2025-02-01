# def to5(x: int):
#   s = ''
#   while x > 0:
#     s += str(x % 5)
#     x //= 5
#   return s[::-1]
# print(sum([int(x) for x in to5(5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3)]))


# for x in '0123456789ABCDEFGHI'[::-1]:
#   res = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
#   if res % 18 == 0:
#     print(res // 18)
#     break

# for x in range(2030, -1, -1):
#   res = 3 ** 100 - x
#   s=''
#   while res > 0:
#     s +=str(res % 3)
#     res //= 3
#   if s.count('0') == 5:
#     print(x)
#     break


# res = 7 * 5 ** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
# s=''
# while res > 0:
#   s += str(res % 5)
#   res //= 5
# print(s.count('4'))


# for x in '0123456789ABCDEFG'[::-1]:
#   res = int(f'5432{x}67', 17) + int(f'302{x}', 17)
#   if res % 19 == 0:
#     print(res)
#     break

# for x in range(10 ** 10):
#
#   res = 9 ** 1942 + 9 * 6 ** 971 + 214 - x
#   s = ''
#   while res > 0:
#     s += str(res % 9)
#     res //= 9
#   s = s[::-1]
#   if abs(s.count('2') - s.count('8')) == 471:
#     print(x)
#     break

res = 2 ** 2048 + 32 ** 102 - 8 * 4 ** 128

ls = []
while res > 0:
  ls.append(res % 32)
  res //=32
alpha = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')[:-4]
ls_res = [i for i in ls if i > 9]
print(len(ls_res))
