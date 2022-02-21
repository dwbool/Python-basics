import random

lst: list = []
for i in range(0, 10):
    t = random.random()

    if (0 < t < 0.33):
        lst.append(int(t * 100.0))
    elif (0.33 <= t < 0.66):
        lst.append(str("some value %.03f" % t))
    else:
        lst.append(float(t))

    print("lst[" + str(i) + "]=" + str(lst[i]) + " is of type " + str(type(lst[i])))
