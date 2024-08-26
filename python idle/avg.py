def avg():
    marks=float(input("Enter the marks"))
    count=1
    tot=0
    avg=0
    while count<10:
        if marks>0:
            tot=tot+marks
            avg=tot/count
            count+=1
            print(tot,avg)
            marks=float(input("Enter the marks"))
        else:
            print("Invalid marks")
    else:
        print("Current total and aveage is : ", tot," ",avg)
