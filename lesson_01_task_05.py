income = float(input("please input company's income "))
expend = float(input("please input company's expenditure "))
revenue: float = income - expend
print("the company's financial result is %s of %.02f" % ("profit" if revenue > 0 else "loss", abs(revenue)))
