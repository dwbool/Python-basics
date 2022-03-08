fname: str = "staff.txt"  # in which lines must be: surname| 123.12
#                                               or: surname 123.12
thr: float = 20000.0  # salary threshold

print("reading: " + fname + "\n------------------")

with open(fname, "r", encoding="utf-8") as f:

    wage_sum = 0
    n_staff = 0
    n_less = 0

    while 1:

        s = f.readline()
        if s == '':
            break
        else:

            lst = s.split('|')

            if len(lst) == 1:
                if len(lst[0]) > 1:
                    lst = s.split(' ')

            if len(lst) == 2:
                surname = lst[0].strip()
                wage = 0
                n_staff += 1
                try:
                    wage = float(lst[1].strip())
                except:
                    print(f"cannot read the wage of {surname} which is {lst[1]}")
                    continue
                if wage < 20000.0:
                    n_less += 1
                    print("%s   earns\t\t\t\t%.02f\t\t\t\twhich is less than %.02f" % (surname, wage, thr))

                wage_sum += wage

    print("-------------\naverage staff member's income is %.2f" % float(wage_sum / n_staff))
    print("there are %d staff member(s) whose wage is less than %.2f" % (n_less, thr))
    print("there are %d staff member(s) in total" % (n_staff))
