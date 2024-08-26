def number():
    num = int(input("Enter the number :"))
    x = 1
    while (x <= num):
        if(x % 10 == 0):
            print(x)
        else:
            print(x, end = " ")
        x += 1
