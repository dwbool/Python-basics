def one_div(a, b):
    if b == 0:
        return None
    return a / b


x = float(input("input x "))
y = float(input("input y "))
s = one_div(x, y)
msg = "x/y = %.16f" % float(s) if s is not None else "Cannot divide by 0"
print(msg)

