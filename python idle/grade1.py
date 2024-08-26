def grade1():
    marks = float(input("Enter your marks obtained for ICT:"))
    if marks >= 75:
        print("Grade A")
    elif 74 >= marks >= 65:
        print("Grade B")
    elif 64 >= marks >= 55:
        print("Grade C")
    elif 54 >= marks >= 35:
        print("Grade S")
    else:
        print("Grade F")
