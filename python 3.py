consultation = int(input("Enter consultation fee: "))
tests = int(input("Enter diagnostic charges: "))
treatment = int(input("Enter treatment charges: "))

total = consultation + tests + treatment

if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

bill = total - discount
paid = int(input("Enter amount paid: "))

print("Total Bill: Rs.", bill)
print("Balance: Rs.", max(0, bill - paid))

if paid >= bill:
    print("Payment Complete")
else:
    print("Payment Pending")