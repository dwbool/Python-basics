lst = []
while 1:
    a = input("input numeric list value or leave blank and press Enter to exit ")
    if a == "":
        break

    try:
        f = float(a)
        lst.append(f)
    except:
        continue

print("list before")
print(lst)

for i in range(0, len(lst) // 2):
    ntx = i * 2
    x = lst[ntx]
    lst[ntx] = lst[ntx + 1]
    lst[ntx + 1] = x

print("list after swapping")
print(lst)
