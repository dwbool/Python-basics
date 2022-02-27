my_list = [7, 5, 3, 3, 2]

while 1:
    try:
        print("current ratings are: %s" % str(my_list))
        x = int(input("input new rating as a Natural number or leave blank to exit and hit Enter: "))

        if x <= 0:
            print("must be a natural number")
            continue

        cnt = my_list.count(x)

        if cnt == 0:
            for i in range(0, len(my_list)):
                if my_list[i] < x:
                    my_list.insert(i, x)
                    break
                elif i == len(my_list) - 1:
                    my_list.append(x)
        else:
            ntx = my_list.index(x)
            my_list.insert(ntx, x)

    except Exception as e:

        print("going to exit as we faced %s" % type(e))
        break
