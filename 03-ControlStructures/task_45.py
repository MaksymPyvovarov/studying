import math

inputNumber = int(input("Enter amount of numbers: "))
root = int(math.sqrt(inputNumber))
x = " 1 "
y = 1
remainder = inputNumber % (root ** 2)
print(remainder)

if remainder == 0 :
    for i in range(root) :
        
        while y != root :
            
            x += str(root * y + 1 + i).rjust(2)
            
            x += " "
            y += 1
        y = 0
        print(x)
        x = ""
if remainder > root :
    for i in range(root + 1) :
        
        while y != (root + 1) :
            
            x += str((root + 1) * y + 1 + i).rjust(2)
            
            x += " "
            y += 1
        y = 0
        print(x)
        x = ""
