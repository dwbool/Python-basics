def is_low(s):
    for i in range(len(s)):
        if s[i].lower() != s[i]:
            return False
    return True


def int_func(s):
    g = ""
    for i in range(len(s)):
        g += s[i].upper() if i == 0 else s[i].lower()
    return g


s = input("input words of small letters, separated by spaces ")
if not is_low(s):
    print("must be of lower case characters")
else:
    lst = s.split(' ')
    res = ""
    for i in range(0, len(lst)):
        res += int_func(lst[i]) if i == 0 else ' ' + int_func(lst[i])
    print(res)
