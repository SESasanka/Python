def university():
    result = input("Did you pass your A/L(yes/no)?")
    if result =="yes":
        english = input("Did you pass English(yes/no)?")
        if english == "yes":
            print("Your are eligible")
        else:
            print("Take your applitude test")
    else:
        print("You are not eligible")
