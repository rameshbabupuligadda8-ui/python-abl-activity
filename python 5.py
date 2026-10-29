data = int(input("Enter required data in GB: "))
budget = int(input("Enter your budget: "))

plan1 = 199
plan2 = 399
plan3 = 599

if data <= 10 and plan1 <= budget:
    print("Choose Plan 1: Rs.", plan1)
elif data <= 25 and plan2 <= budget:
    print("Choose Plan 2: Rs.", plan2)
elif data <= 50 and plan3 <= budget:
    print("Choose Plan 3: Rs.", plan3)
else:
    print("No suitable plan available")