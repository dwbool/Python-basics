lst = []


def add_all(lst):
    sum: float = 0
    for i in range(0, len(lst)):
        sum += float(lst[i])
    return sum


while 1:
    try:

        print("input space separated numbers or leave blank to exit, q=sum and quit c=list clear ")
        s = input()
        if s == "":
            break
        slst = s.split()
        do_quit: bool = 0
        for i in range(0, len(slst)):
            sx = slst[i]
            if sx == 'q':
                do_quit = True
                break
            if sx == 'c':
                lst.clear()
                print("emptying the list")
                continue
            num = float(sx)
            lst.append(num)

        sum = add_all(lst)
        print("sum %s = %s" % (str(lst), sum))
        if do_quit:
            print("going to quit the program")
            break

    except Exception as e:
        print("we faced error " + str(e))
        continue

