from functools import reduce
#
src = [x for x in range(100, 106 + 1) if x % 2 == 0]
dst = reduce(lambda x, y: x * y, src)

print(src)
print("product of all elements %s" % str(dst))
