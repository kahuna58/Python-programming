#eligbilty in kenya, uganda and Tanzania
age=int(input("enter your age:"))
citizenship=input("enter citizenship:")
if age>=18 and citizenship in ["Kenyan", "Ugandan","Tanzanian"]:
    print("Eligible to vote")
else:
    print("Not eligible")
