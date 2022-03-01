income = float(input("please input company's income $ "))
expend = float(input("please input company's expenditure $ "))
revenue: float = income - expend

print("the company's financial result is %s of %.02f" % ("profit" if revenue > 0 else "loss", abs(revenue)))

if revenue > 0:
    num_emp = int(input("please input company's employee number "))
    profitability = revenue / income * 100.0
    per_cap = revenue / num_emp
    print(f"the company's profitability is {profitability:.3f} %, revenue per employee is $ {per_cap:.2f} ")


