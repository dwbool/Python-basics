import itertools
#
for x in itertools.count(10, 20):
    print(x, end=' ')
    if x > 200:
        break

print()
n = 0
for x in itertools.cycle([1, 2, 4, 8]):
    n += 1
    if n > 20:
        break
    print(x, end=' ')
