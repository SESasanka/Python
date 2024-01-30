gender = input("Enter the gender:")
age = int(input(" enter your age:"))
if age <18: 
    if gender == 'M':
        print('Son')
    else:
        print('daughter')
elif age >=18 and age <65:
    if gender == 'M':
        print ('fater')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
