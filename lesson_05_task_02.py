fname:str = "notes.txt"
print("reading: " + fname)

with open(fname, "r", encoding="utf-8") as f:
    n_lin = 0
    n_word_total = 0

    while 1:

        s = f.readline()
        if s == '':
            break
        else:
            n_lin += 1
            lst = s.split(' ')
            n_word = 0

            for wrd in lst:
                if wrd.strip() != '':
                    n_word += 1
                    n_word_total += 1

            s = s.strip()
            s += "\t\t\t\t : line %d contains %d word(s)\n" % (n_lin, n_word)
            print(s, end='')

print("------------------\ntotally there are %d line(s) and %d word(s) in %s" % (n_lin, n_word_total, fname))
