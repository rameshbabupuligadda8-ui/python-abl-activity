material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter total selling price: "))

total_cost = material + labour + machine
profit = selling - total_cost

print("Total Cost: Rs.", total_cost)
print("Profit: Rs.", profit)

if profit >= 10000:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")