def grade():
    marks = float(input("Enter your marks obtained for ICT "))
    if marks >= 75 :
        print("Grade A")
    elif 65 <= marks <= 74:
        print("Grade B")
    elif 55 <= marks <= 64:
        print("Grade C")
    elif 35 <= marks <= 54:
        print("Grade s")
    else:
        print("Grade F")
        
