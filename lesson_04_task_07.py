def fact_generator(n):
    f = 1
    for el in range(1, n + 1):
        f *= el
        yield f

#
def fact_prn(n):
    g = fact_generator(n)
    for i in g:
        print(i, end=' ')


N = 10
print("factorials from 1! to %d!" % N)
fact_prn(N)
