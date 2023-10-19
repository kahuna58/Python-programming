#marks allocation program
math=int(input("Enter math: "))
eng=int(input("Enter eng: "))
kisw=int(input("Enter kisw: "))
average=float(input((math+eng+kisw)/3))
if average>70 and average<100:
    print("A")
if average>60 and average<69:
    print("B")
if average>50 and average<59:
    print("C")
