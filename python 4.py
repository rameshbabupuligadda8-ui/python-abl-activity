basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives
deduction = gross * 0.10
net_salary = gross - deduction

print("Gross Salary: Rs.", gross)
print("Deduction: Rs.", deduction)
print("Net Salary: Rs.", net_salary)