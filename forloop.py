def temp():
    temp = float(input("Enter the temp :"))
    method = input("If you want to covert from Fahrentheit to Celsius, type FC or CF :" )
    while temp < 100:
        if method == "FC":
            f = 1.8 * temp + 32
            print(f)
            temp = float(input("Enter the temp :"))
            method = input("If you want to covert from Fahrentheit to Celsius, type FC or CF :" )
        elif method == "CF":
            cel = (temp-32)/1.8
            print(cel)
            temp = float(input("Enter the temp :"))
            method = input("If you want to covert from Fahrentheit to Celsius, type FC or CF :" )
        else:
            print("Choose a valid method")
            temp = float(input("Enter the temp :"))
            method = input("If you want to covert from Fahrentheit to Celsius, type FC or CF :" )

    else:
        print("Enter valid Temp")
        temp = float(input("Enter the temp :"))
        method = input("If you want to covert from Fahrentheit to Celsius, type FC or CF :" )
    return temp()
        
