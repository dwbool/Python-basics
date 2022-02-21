from typing import List, Any

goods: list[Any] = []
anl: dict = {}

index = 0

while 1:
    print("input piece of goods data or leave the name blank and hit Enter: ")
    name = input("input name ")
    if name == "":
        print("exiting the program...")
        break
    price = input("input price ")
    quantity = input("input quantity ")
    un = input("input unit ")

    dct = {"name": name, "price": price, "quantity": quantity, "unit": un}
    index += 1
    goods.append((index, dct))
    names = []
    prices = []
    quantities = []
    uns = []

    print("current goods:")

    for g in goods:
        print(g)
        names.append(g[1]["name"])
        prices.append(g[1]["price"])
        quantities.append(g[1]["quantity"])
        uns.append(g[1]["unit"])

    print("current analytics:")
    anl["name"] = names
    anl["price"] = prices
    anl["quantity"] = quantities
    anl["unit"] = uns

    for key in anl:
        line = str(anl[key])
        print("\"%s\" : %s" % (key, line))
