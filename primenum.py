num = int(input("Enter Number : "))

if num < 2:
    print("Not prime")

elif num > 2:
    prime = num
    while num > 2:
        num -=1
        rem = prime % num
        if rem == 0:
            print("Not prime")
            break
        if num == 2:
            print("prime")
else:
    print("prime")
    