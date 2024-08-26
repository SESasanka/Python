def chore_bonus():
    bags = int(input("How many bags of leaves did you fill this month?"))
    if (bags >= 10):
        total = bags * 3 + 20
    else:
        total = bags * 3
    print ("Great, you made $" + str(total) + ".")
     
