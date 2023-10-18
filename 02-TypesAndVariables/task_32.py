x = input("Amount: ")
vatPercentage = input("VAT precentage: ")
vat = round((float(x) * float(vatPercentage) / 100), 2)

print(f"VAT {vatPercentage}%: ",round(vat, 2))