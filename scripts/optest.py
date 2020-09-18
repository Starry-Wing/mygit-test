days=int(input("Enter days:"))
months=days//30
days=days%30
years=months//12
print("years={},months={},days={}".format(years,months,days))

