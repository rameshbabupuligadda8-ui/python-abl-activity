marks = int(input("Enter aggregate marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 250000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")