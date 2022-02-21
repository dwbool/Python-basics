month_season = []
month_dict = {}

for i in range(1, 13):
    season = ""
    if i <= 2 or i == 12:
        season = "winter"
    elif i < 6:
        season = "spring"
    elif i < 9:
        season = "summer"
    else:
        season = "autumn"
    month_season.append(season)
    month_dict[i] = season

print(month_season)
print(month_dict)

n = abs(int(input("input month number 1-12 : ")) - 1) % 12

print("using List, your month belongs to %s" % month_season[n])

print("using Dictionary, your month belongs to %s" % month_dict[n + 1])
