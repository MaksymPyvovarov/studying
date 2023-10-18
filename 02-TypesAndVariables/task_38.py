x = input("Enter phone number: +")
y = str("")
xq = 0

for i in range(int(len(x) / 3)) :
    for j in range(3):
        y += x[j + xq]
    if j + xq == len(x) - 1 :
            break
    y += "-"
    xq += 3
    
print(y)
