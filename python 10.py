venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
food = float(input("Enter catering cost: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_cost = venue + equipment + food
remaining = total_cost - sponsorship

print("Total Event Cost: Rs.", total_cost)
print("Remaining Cost: Rs.", max(0, remaining))

if fee > 0:
    students = max(0, int(remaining / fee))
    if students * fee < remaining:
        students += 1
    print("Minimum Registrations Needed:", students)
else:
    print("Registration fee must be greater than zero")