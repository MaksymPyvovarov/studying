x = int(input("Enter the amount of PLN: "))
print(f"The amount of PLN {x} in coins: ")

if x >= 5 :
    fiveGroszy = int(x / 5)
    remainder5 = x % 5
    print(f"5 zł - {fiveGroszy}")

if x >= 2 and x < 5 :
    twoGroshy = int(x / 2)
    remainder2 = twoGroshy % 2
    print(f"2 zł - {twoGroshy}")

if x >= 2 and x >= 5 :
    twoGroshy = int(fiveGroszy / 2)
    remainder2 = fiveGroszy % 2
    print(f"2 zł - {twoGroshy}")
if x > 1 :
   oneGroszy = int(remainder2 / 1)
   print(f"1 zł - {oneGroszy}")
else : 
    print(f"1 zł - {1}")

