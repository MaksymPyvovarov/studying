
count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input("Enter number: "))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Quantity =",count - 1, "Sum =",sum, "Mean =", sum / (count-1))
	