fname: str = "nums.txt"

print("reading: " + fname + "\n------------------")

sum: float = 0

with open(fname, "r", encoding="utf-8") as f:
    while 1:

        s = f.readline()
        print("\n" + s.strip())

        if s == '':
            break
        else:
            lst = s.split(' ')
            print("summation: ", end='')
            for sn in lst:
                try:
                    n = float(sn.strip())
                    sum += n
                    print("%f " % n, end='')
                except Exception as e:
                    print("bad num " + sn + "\nmsg: "+str(e))

print("----------\nsum = %.6f" % sum)
