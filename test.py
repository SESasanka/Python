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

# L=[10, 20, 34, 47, 54]
# count=0
# sumOfNumber=0
# k=int(input('Enter K Value : '))
# for i in range(len(L)):
#     if L[i] < k:
#         count+=1
#         sumOfNumber+=L[i]
#         i+=1
#     avg = sumOfNumber/count
# print(avg)

# def calculate(n):
#     Results = 0
#     for i in range(1, n+1):
#         for j in range(i):
#             Results += i * j
#     return Results

# print(calculate(4))

# data = [5,1,23,10,-3]
# def fun(a):
#     i,c =1,a[0]
#     while i < len(a):
#         if a[i] > c:
#             c = a[i]
#         i += 1
#     return c
# print(fun(data))

# data = [5,1,23,10]
# datacount = len(data)
# for i in range(datacount-1):
#     for j in range(i,datacount):
#         if data[i]>data[j]:
#             data[i],data[j] = data[j],data[i]
# for i in range(datacount):
#     print(data[i])

# def list_operations(nlist):
#     for i in range(len(nlist)):
#         if i %+2==0:
#             nlist[i]**=2
#         else:
#             nlist[i]+=3
#     return nlist
# numbers=[1,2,3,4,5]
# output= list_operations(numbers)
# print(output)

# marks=[(1,"amara",96),(2,"rajah",34),(3,"rani",49),(4,"faahim",68)]
# i=-1
# while i < len(marks)-1:
#     i+=1
#     if marks[i][2]<50:
#         continue
#     print(marks[i][1],end=" ")

# def factorial(num):
#     x=1
#     fact = num
#     while x < num:
#         fact *=x
#         x+=1
#     return fact

# n = int(input("Enter Number : "))
# print(factorial(n))

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#     return fact

# num = int(input("Enter Number : "))
# print(factorial(num))

# i=1
# tot=0
# while i<=5:
#     x=int(input(f"Enter Number {i} : "))
#     tot=tot+x
#     i=i+1
# print(tot)

# temp=[23,45,2,-2,0]
# print(temp[:2])

# x = 1
# while x < 1024:
#     x*=2
# print(x)


# def calculate(n):
#     return n // 2
# for i in range(1,6):
#     print(calculate(i), end=',')

# def sss(n):
#     if n<=1:
#         return n
#     else:
#         return sss(n-1)+sss(n-2)
# print(sss(3))

# for i in range(5):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i,end=',') 

# result = [x+"2" for x in '123']
# print(result)


# def calc(a,b,c):
#     return(a**b // c+2) + 5.2 - 4.2
# print(calc(2,5,1))

# a = 2
# b = 5
# c = 1

# print(a**b // c + 2)

# def myfunc(*data):
#     temp=0
#     for i in data:
#         temp+=i
#     return temp
# print(myfunc(4,8,3.25,6,-1,9,-3))

# thislist = ["apple","banana","cherry"]
# for i in thislist:
#     print(i)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# i = 0
# while i < len(fruits):
#     print(fruits[i], end=" ")
#     i += 1

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(31):
#     print(fibonacci(i))

# count = 1
# maxnum = 0
# while count <=10:
#     num = int(input(f"Enter Number {count} : "))
#     if num > maxnum:
#         maxnum = num
#     count += 1
# print(f"Maximum number is : {maxnum}")

# for i in range(1,11):
#     num = int(input(f"Enter number {i} : "))
#     if num > maxnum:
#         maxnum = num
#     count+=1
# print(f"Maximum number is {maxnum}")

# mytuple = ("abc","def","ghi")
# myit = iter(mytuple)
# for i in mytuple:
#     print(i)


# word = str(input("Enter Palidrome Word : "))
# if word == word[-1::-1]:
#     print(f"This word {word} is Palidrome")
# else:
#     print("Not a palidrome word")

# word = "madam"
# word1 = word[-1::-1]
# print(word1)

# prime = 0
# for i in range(2,10):
#     rem = 0
#     for j in range(2,i):
#         if i % j == 0:
#             rem += 1
#     if rem == 0:
#         print(f"{i} is Prime Number")


# def bubble_sort(lst):
#     for i in lst:
#         i=0
#         while i < len(lst)-1:
#             if lst[i] > lst[i+1]:
#                 lst[i],lst[i+1]=lst[i+1],lst[i]
#             i+=1
#     return lst

# l = []
# n = int(input())
# while n > 0:
#     l.append(n)
#     n= int(input())
# m=min(l)
# F=False
# while m>=1 and not F:
#     for K in l:
#         if K%m == 0:
#             F=True
#         else:
#             F=False
#         if not F:
#             break
#     m-=1
# print(m+1)

# for x in [0,1,2]:
#     for y in [0,1]:
#         print("*")

# def mystery(str):
#     out = ''
#     for char in str:
#         if char == 'i':
#             break
#         if char == 'a':
#             continue
#         out+=char
#     return out
# print(mystery('walking'))

# def fun1():
#     x = 10
#     return x

# def fun2():
#     x = 20
#     return x

# total = fun1() + fun2()

# print(total)

# def SD(L):
#     tot=0
#     for i in L:
#         avg=sum(L)/len(L)
#         x=(i-avg)**2
#         tot+=x
#         sd=(tot/len(L)-i)**0.5
#     return sd,avg
# data=[10,12,14,16,18,20]
# stddev,average=SD(data)
# print(f"Standard Deviation: {stddev}, Average: {average}")

# for x in range(6,0,-2):
#     print(x,end=',')

# numbers=[22,34,12,32,4]
# sum=0
# i = len(numbers)
# while (i!=0):
#     i-=1
#     sum+=numbers[i]
# print(sum, end='')

# def example1(a):
#     if a == 1:
#         return 1
#     else:
#         return a * example1(a - 1)
# print(example1(3))

# name='nimal'
# if len(name) > 3:
#     print('nice name')
#     print(name)
# else:
#     print('short name')
#     print(name)

# x={1,2,3}+{4,5,6}
# print(x)

# num=2
# while num < 10:
#     print(num)
#     num+=2

# a=[1,2,3,None,(),[]]
# print(len(a))

# x=4.5
# y=2
# print(x//y)

# x="welcome to python".split()
# print(x)

# for i in range(9,1,-1):
#     if i == 5:
#         continue
#     else:
#         print(i,end=',')

# list1=[0.5 * x for x in range(0,4)]
# print(list1)

# names=["Nimal","Sunil","Amara","Kumara"]
# sum=0
# for ls in names:
#     if  ls=="Nimal":
#         sum+=1
#     if ls=="Sunil":
#         sum+=10

# print(sum)

a=2**2**3//4.0*(8/4)
print(a)