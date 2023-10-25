y = "0805"

for i in range(3) :
    x = str(input("Enter the PIN code: "))
    if x == y :
        print("Welcome")
        break
    else :
        print("Incorrect...")
if x != y :
    print("Sorry, you payment card has been blocked")