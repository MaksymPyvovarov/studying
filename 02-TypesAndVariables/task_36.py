x = float(input("Bank buys EUR: "))
y = float(input("Bank sells EUR: "))
xy = y - x

print(y - x)
print("Spread: ", format(round(xy, 4), ".4f"))