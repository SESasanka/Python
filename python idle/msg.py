def msg():
    msg1 = "outside of loop"
    msg2 = "I am in a while loop"
    counter = 0
    print(msg1)
    while (counter < 10):
        print(msg2)
        counter += 1
    print(msg1)
