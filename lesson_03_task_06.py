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


s = input("input word of small letters ")
if not is_low(s):
    print("must be of lower case characters")
else:
    print(int_func(s))
