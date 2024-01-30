current_year = int(input("enter the year :"))
month = int(input("enetr the month :"))
if ((current_year % 4) == 0 and (current_year % 40) == 0 and (current_year % 400) == 0):
    print("leap year")
    if (month == 1 or month == 5 or month == 7 or month == 8 or month == 11 or month == 12):
        print("There are 31 days in this month")
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        print("There are  30 days in this month ")
    elif (month == 2):
        print("There are 29 days in this month")
    else:
        print("Invalid month")
elif ((currnt_year % 4) != 0 or (current_year % 100) != 0 or (current_year % 400) != 0):
    print("There are 31 days in this month ")
    if (month == 1 or month == 2 or month == 3):
        print("There are 31 days in this month")
    elif (month == 4 or month == 6 or month == 9 or month == 11):
        print("There are 30 days in this month")
    elif (month == 2):
        print("There are 20 days in this month ")
    else:
        print("Invlid month")
else:
    print("Invalid year")
