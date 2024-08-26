def year():
    currentyear = int(input("Enter the year:"))
    month = int(input("Enter the month:"))
    if((currentyear % 4) == 0 and (currentyear % 100) != 0 or(currentyear % 400) == 0):
        print("Leap year")
        if( month == 1 or month == 3 or month == 5 or month == 7 month == 8 or month == 10 or month == 12):
            print("There are 31 days in this month")
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            print("There are 30 days in this month")
        elif (month == 2):
            print("There are 29 days in this month")
        else:
            print("Invalid month")
    elif((currentyear % 4) != 0 or (currentyear % 100) != 0 or (currentyear % 400) != 0):
        print("Non leap year")
        if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
            print ("There are 31 days in this month")
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            print("There are 30 days in this month")
        elif(month == 2):
            print("There are 28 days in this month")
        else:
            print("Invited month")
    else:
        print("Invited year")
                  
