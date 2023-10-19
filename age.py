person1=int(input("Enter person1 age"))
person2=int(input("Enter person2 age"))
person3=int(input("Enter person3 age"))

if person1 > person2 and person3:
    print("person1 is the oldest")

if person2 > person1 and person3:
    print("person2 is the oldest")

if person3 > person2 and person1:
    print("person3 is the oldest")
