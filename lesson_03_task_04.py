def my_func(x, y):
    x = float(x)
    y = float(y)
    if y > 0:
        return None
    yp = int(abs(y))
    prod: float = 1
    for i in range(0, yp):
        prod *= x
    return 1.0 / prod


def my_func2(x, y):
    x = float(x)
    y = float(y)
    if y > 0:
        return None
    return x**y


x, y = input('input x and y separated by space (y must be negative integer or 0): ').split()
if float(y) <= 0:
    print("x^y = %s" % str(my_func(x, y)))
    print("x**y = %s" % str(my_func2(x, y)))
else:
    print("y must be negative integer or 0")
