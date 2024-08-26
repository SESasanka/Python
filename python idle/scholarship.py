def scholarship():
    SAT_score = int(input("What is your SAT score?"))
    if (SAT_score > 1100):
        GPA = float(input("What is your GPA?"))
        if (GPA > 3.0):
            print("Great, Your qualify for the scholarship!")
        else: 
            print("Sorry , You don't qualify for the scholarship")
