x = int(input("Enter number of prime numbers: "))
array = [2, 3, 5, 7]
returnArray = []
number = 2
count = 0

if x >= 4 :
    for i in range(4) :
        returnArray.append(array[i])
    while count != x - 4 :
        if (number % 2) == 0 or (number % 3) == 0 or (number % 5) == 0 or (number % 7) == 0 :
            number += 1
        else :
            returnArray.append(number)
            count += 1
            number += 1
else : 
    for i in range(x) :
        returnArray.append(array[i])

print("Prime numbers:",returnArray)