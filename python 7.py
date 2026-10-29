price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

tax = (total - discount) * 0.05
final_bill = total - discount + tax

print("Total Price: Rs.", total)
print("Discount: Rs.", discount)
print("Tax: Rs.", tax)
print("Final Bill: Rs.", final_bill)