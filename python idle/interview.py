def interview():
    Q1 = input("Do you have an academic qualification?(yes/no)")
    Q2 = input("Do you have professional Qulification?(yes/no)")
    Q3 = int(input("How many years of work experience do you have?"))
    if(Q1 == 'yes' and Q2 == 'yes' or Q3 >=2):
        print("you are employee")
    elif (Q3 < 2 and Q1 == 'yes'):
        print("you are an intern")
    elif (Q3 < 2 and Q2 == 'yes'):
        print("you are an assistain")
    else:
        print("Please apply next time.")
