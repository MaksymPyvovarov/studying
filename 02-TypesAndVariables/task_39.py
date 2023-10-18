price = input("Enter price: ")
discount = input("Enter discount %: ")

#print(f"Enter price: {price}")
#print(f"Enter discount %: {discount}")

priceAfterDiscount = float(price) - (float(price) * float(discount) / 100)

print("Price with discount: ",round(priceAfterDiscount, 2))

reduction = float(price) * float(discount) / 100

#print("Reduction: ",format(round(reduction, 2), '.2f'))


print("Reduction {0: .2f}".format(round(reduction, 2)))