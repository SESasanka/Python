n = int(input("Enter the maximum limit value: "))
for num in range(1, n + 1):
    if num % 2 == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))
