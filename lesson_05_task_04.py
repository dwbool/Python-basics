

fname: str = "onetwo.txt"
fname_out: str = "one_vernacular.txt"

print("reading: " + fname + "\n------------------")

with open(fname, "r", encoding="utf-8") as f, open(fname_out, "w", encoding="utf-8") as fout:
    while 1:

        s = f.readline()
        print(s.strip())

        if s == '':
            break

        lst = s.split(' ')

        if len(lst) == 3:
            snum = lst[0].strip().lower()
            svern = ""
            if snum == "one":
                svern = "один"
            elif snum == "two":
                svern = "два"
            elif snum == "three":
                svern = "три"
            elif snum == "four":
                svern = "четыре"
            elif snum == "five":
                svern = "пять"
            elif snum == "six":
                svern = "шесть"
            elif snum == "seven":
                svern = "семь"
            elif snum == "eight":
                svern = "восемь"
            elif snum == "nine":
                svern = "девять"
            elif snum == "ten":
                svern = "десять"

            n: int = -1
            try:
                n = int(lst[2])
            except:
                print("wrong number " + lst[2])

            if len(svern) > 0 and n > -1:
                sres = "%s %s %d\n" % (svern.capitalize(), lst[1], n)
                print(sres, end='')
                fout.write(sres)

print("---------------\nvernacular numbers are written to: " + fname_out)
