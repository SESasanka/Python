def school_trip():
    letter = input("Do you have permission letter?")
    fee = int(input("How much did you pay for the trip?"))
    if letter == "yes" and fee >= 3000:
        print("You can go on the trip and you balance is ", fee-3000)
    elif letter == "yes" and fee < 3000:
        print("You can go on the trip and you balance is ", fee-3000)
    else:
        print("You cannot join the trip.")
