x = input("Enter name, surname and date of birth: ")
y = x.split()
initials = str("")

if y[0] == "Mr." or y[0] == "Mrs." : 
    name = y[1]
    surname = y[2]
    dateOfBirth = y[len(y) - 1]
else: 
    name = y[0]
    surname = y[1]
    dateOfBirth = y[len(y) - 1]
initials += name[0]
initials += surname[0]

print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Initials: {initials}")
print(f"Born: {dateOfBirth}")

#name = input("Enter name: ")
#surname = input("Enter surname: ")
#born = input("Date of birth: ")#

#initials = name[0] + surname[0]#
#

#print(f"Name: {name}")
#print(f"Surname: {surname}")
#print(f"Initials: {initials}")
#print(f"Born: {born}")