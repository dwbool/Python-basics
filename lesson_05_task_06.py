
fname: str = "subjects.txt"

print("reading: " + fname + "\n------------------")

dct_subj ={}

with open(fname, "r", encoding="utf-8") as f:
    while 1:

        s = f.readline()
        print("\n" + s.strip())

        if s == '':
            break
        else:
            lst = s.split(':')
            if len(lst) == 2:
                subj = lst[0]
                print("subject: %s" % subj, end='')
                sum: float = 0
                lst_time= lst[1].split(' ')
                for sn in lst_time:
                    if len(sn.strip()) == 0:
                        continue
                    lst_rec = sn.split('(')
                    if len(lst_rec) > 0:
                        n = 0
                        try:
                            n = float(lst_rec[0])
                        except:
                            print(" bad_num:"+lst_rec[0])
                        sum += n

                print(", hours: %f" % sum)
                dct_subj[subj] = sum


print("----------\nsubject dictionary: %s" % str(dct_subj))
