def Field_Trip():
    slip = input("Did you bring back your signed permmison slip(yes/no)?")
    if slip == "yes":
        history_question = input("Which number amendment allowed women to vate in the US?")
        if history_question == "19":
            print("You will get to go to the History museum")
        else:
            print("You will get to go to the Art museum")
    else:
        print("Sorry , Your can't go to the field trip without a signed permission.")
