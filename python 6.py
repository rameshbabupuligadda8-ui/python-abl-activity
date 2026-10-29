distance = int(input("Enter travel distance in km: "))
age = int(input("Enter passenger age: "))

fare = distance * 2

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75

fare = fare + 30

print("Railway Fare: Rs.", fare)