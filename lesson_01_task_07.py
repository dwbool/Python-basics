a = float(input("please input initial distance "))
b = float(input("please input desired distance "))
growth: float = 0.1
nday: int = 1

while a < b:
    a += a * growth
    nday += 1

print("the day number when you will achieve the desired distance is {}".format(nday))
