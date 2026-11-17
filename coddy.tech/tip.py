var1 = float(input("Bill is:"))
var2 = float(input("Tip Precentage:"))
var3 = int(input("How many ways is the bill being split?"))
tip_amount = (var2 / 100) * var1
total = var1 + tip_amount
print(f"${total}")
total = total / var3
print(f"${total:,.2f}")