a = int(input("Enter a: "))
b = int(input("Enter b: "))

x = ""
y = "*"
for i in range(b) : 
    x += "* "

for j in range(int(b - 2)) : 
    y += "  "
y += " *"

print(x)
for g in range(int(a - 2)) :
    print(y)
print(x)