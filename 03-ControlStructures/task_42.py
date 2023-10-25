x = int(input("Enter number of display numbers: "))

num1 = 0
num2 = 1
count = 2
sum = 0
returnNumber = ""


if x == 1 :
    returnNumber = str(num1)

elif x == 2 :
    returnNumber += str(num1)
    returnNumber += " "
    returnNumber += str(num2)
else :
    returnNumber += str(num1)
    returnNumber += " "
    returnNumber += str(num2)
    returnNumber += " "
    while count != x :
        sum = num1 + num2
        returnNumber += str(sum)
        returnNumber += " "
        num1 = num2
        num2 = sum
        count += 1


print(returnNumber)
    