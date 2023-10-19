#bonus program
Amount=int(input("persons salary: "))
time = int(input("time period of service: "))
bonus=amount * time

if time>10:
    bonus=0.08 * salary
    print("bonus is",bonus)
elif time >=6 and time <=10:
        bonus=0.08 * salary
     print("Amount * 0.08")
else:
    print("Amount * 0.05")
