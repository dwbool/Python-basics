def sum_2max3(*arg):
    if len(arg) != 3:
        return None
    try:
        a, b, c = float(arg[1]), float(arg[0]), float(arg[2])
        if b > a:
            a, b = b, a
        if c > b:
            b = c
        return a + b
    except Exception as e:
        return None


try:
    print("input 3 numbers: ")
    a = float(input("input a "))
    b = float(input("input b "))
    c = float(input("input c "))
    print("sum of 2 highest numbers is " + str(sum_2max3(a, b, c)))
except Exception as e:
    print("we faced some error "+str(e))

