import json

fname: str = "firms.txt"
fname_out: str = "firms.json"

print("reading: " + fname + "\n------------------")

sum_rev = 0.0
n_firm = 0
dct_firm = {}

with open(fname, "r", encoding="utf-8") as f:
    while 1:

        s = f.readline()
        print("\n" + s.strip())

        if s == '':
            break
        else:
            lst = s.split(' ')
            if len(lst) == 4:
                name = lst[0]
                frm = lst[1]
                profit = 0.0
                expend = 0.0
                try:
                    profit = float(lst[2])
                    expend = float(lst[3])
                except:
                    print("bad_num")

                print("firm: %s %s %s %s" % (name, frm, profit, expend), end='\n')
                revenue: float = profit - expend
                if revenue > 0:
                    sum_rev += revenue
                n_firm += 1
                print("revenue %.2f" % revenue)

                dct_firm[name] = revenue

    aver_rev = sum_rev / n_firm if n_firm > 0 else 0
    print("average revenue %.2f" % (aver_rev))

    dct_aver = {}
    dct_aver["average_profit"] = aver_rev
    lst_fin = []
    lst_fin.append(dct_firm)
    lst_fin.append(dct_aver)

    print(lst_fin)
    with open(fname_out, "w", encoding="utf-8") as fjson:
        json.dump(lst_fin, fjson)

    print("\ninformation saved to: " + fname_out)
