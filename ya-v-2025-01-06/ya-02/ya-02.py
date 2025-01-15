print("     a", "b", "c", "d")
i = 0
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if not(((a and b) <= c) and ((b and c) <= d)):
                    i += 1
                    print(i, "->", a, b, c, d)


#   OUTPUT
#      a b c d
# 1 -> 0 1 1 0
# 2 -> 1 1 0 0
# 3 -> 1 1 0 1
# 4 -> 1 1 1 0

# d b a c  <--- Answer
# _ 1 1 1 0
# _ 1 _ 1 0
# 1 1 1 _ 0
# _ 1 1 _ 0