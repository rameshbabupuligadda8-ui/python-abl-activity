dollars = float(input("Enter expense in USD: "))
rate = float(input("Enter USD to INR exchange rate: "))
budget = float(input("Enter travel budget in INR: "))

rupees = dollars * rate
fee = rupees * 0.02
total = rupees + fee

print("Travel Expense: Rs.", total)

if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")