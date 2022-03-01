n = int(input("please input an integer positive number "))
dgt_max: int = 0
while n > 0:
    dgt = n % 10
    if dgt > dgt_max:
        dgt_max = dgt
    n //= 10

print("maximal digit is %d" % dgt_max)
