# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# list_a =[5,15,20,16,8]

# def f(x):
#     total = 0
#     for i in x:
#         total = total+i
#         if total >= 50:
#             break
#     return (total)
# print(f(list_a))


# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(mylist)
# for i in range(n-1):
#   for j in range(n-i-1):
#     if mylist[j] > mylist[j+1]:
#       mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist)


# even = 0
# count = 0
# x = 2

# while x < 10:
#     even += 2
#     # print(even)
#     count = count+even
#     x+=2
# print(f"count {count}")

# count = 0
# i =1

# for i in range(i,10):
#     inputNum = int(input(f"Enter Number {i} : "))

#     count += inputNum
# print(f"Ten numbers count is {count}")


# fact = 0
# num = 0

# num = int(input("Enter Number : "))

# fact = num

# while num > 1:
#     num -= 1
#     fact *=num
# print(fact)


# num = int(input("Enter Number: "))

# if num <= 1:
#     print("This number is not Prime")
# else:
#     i = 2
#     is_prime = True

#     while i < num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

#     if is_prime:
#         print("This number is Prime")
#     else:
#         print("This number is not Prime")


# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact


# num = int(input("Enter number : "))
# if num < 0:
#     print("Factorial is not defiend")
# else:
#     print(f"Factorial of {num} is {factorial(num)}")


# rs = 0
# ar = []
# for i in range(1,5):
#     rs = int(input(f"Enter Result {i} : "))
#     ar.append(rs)
# print(ar)
# print(len(ar))

# tot = 0

# for i in range(1,11):
#     num = int(input(f"Enter Number {i} : "))
#     tot+=num
# print(f"Total of ten number is {tot}")


# l = [2,5,4,3,1]

# for i in range(len(l)):
#     for j in range(len(l)-1):
#       if  l[j] < l[j+1]:
#          l[j],l[j+1]=l[j+1],l[j]

# print(l)


# def additem(numbers):
#     numbers+=[2]

# mylist=[12,16,18,20,24]
# additem(mylist)
# print(len(mylist))

# a = [0,1,2,3]
# for a[-1] in a:
#     print(a[-1],end='')

# a = int(input("Enter number"))
# b = int(input("Enter number"))

# if a<b:
#     a,b=b,a
# d=a-b

# while d>3:
#     print(d)
#     d=d-b