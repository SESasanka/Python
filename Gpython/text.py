# x = 5
# y = "John"
# print(x)
# print(y)

# x = 4   
# x = "Sally" 
# print(x) 
# print(x)

# myVariableName = "John" #Camel Case
# MyVariableName = 9     #Pascal Case
# my_variable_name = "John"  #Snake Case


# x, y, z = "Orange", "Banana"
# print(x)
# print(y)
# print(z)

# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)

# x = "awesome"

# def myfunc():
#   global x
#   x = "well"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)


# x = 5
# y = int(x) + 3
# print(y)

# x = "It's alright"
# print("It's alright")

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
# '''
# print(a)


# a = "Hello, World"
# print(len(a))   13
# print(a.upper())  HELLO, WORLD!
# print(a.lower())  hello, world!
# print(a.title())   Hello, World!
# print(a.capitalize())  Hello, world!
# print(a.center(50))                 hello, World!
# print(a.count("l"))     3
# print(a.startswith("h"))  True or False
# print(a.endswith("h"))  True or False
# print(a.find("o"))  4
# print(a.index("o"))  4

# print(a.istitle()) True or False
# print(a.islower()) 
# print(a.isupper()) 
# print(a.isnumeric()) 
# print(a.isalnum()) 
# print(a.isspace()) 

# x = "Welcome to the game"
# x = "Welcome-to-the-game"

# print(x.split())   ['Welcome', 'to', 'the', 'game']
# print(x.split("-"))  ['Welcome', 'to', 'the', 'game']

# y = "                python                   "

# print("Hello ",y.strip())  Hello  python


# x = "nimal-80\n"

# print(x.split("-")) ['nimal', '80\n']
# print(x.strip().split("-")) ['nimal', '80']


# print('I\'m Nimal')
# print("This will insert one \\ (backslash).") 
# print("Other escape characters\n used in Python:")
# print("Other escape \rcharacters used in Python:")

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# x = "Apple"
# y = 60

# z = "This {} is {} rupees"
# print(z.format(y,x))

# z = "This {} is {} rupees.".format(x,y)
# print(z)

# z = "This %s is %d rupees" % (x,y)
# print(z)

# %s = string 
# %d = decimal 
# %f = float  

# x += 1 ---> x = x + 1
# y -= 2 ---> y = y - 1
# *=	x *= 3	x = x * 3
# print(x // y) 

# 101
# 011
# ----
# 111  ---> 7

# x = 185 #185 

# # x >>= 3   #right shift

# print(x)

# x = 5
# y = 5

# print(x == y)


# x = [1,3,2,4,5]

# print(len(mylist))
# x.append(6)    [1, 2, 3, 4, 5, 6]
# x.clear()     []
# print(x.count(4))  1
# x.extend([6,7,8])   [1, 2, 3, 4, 5, 6, 7, 8]
# y = x.index(3)   2
# x.insert(2,8) 
# x.pop(2)   [1, 2, 4, 5]
# x.remove(3)  [1, 2, 4, 5]
# x.reverse()   [5, 4, 3, 2, 1]
# x.sort(reverse=False)
# print(x) 

# x = (1,6,3,5,3,2,4,5)
# print(len(x))   7
# print(x.count(3))   3
# print(x.index(5))   3
# print(sorted(x))  #[1, 2, 3, 3, 4, 5, 5, 6]
# print(x[2:5])   (3, 5, 3)
# print(x[-4:-1])    (3, 2, 4)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("beri")
# x = tuple(y)
# print(x)

# x = {1:1,"abc":4,3:5}
# x.update({4:6})
# x.pop(2)    {1: 1, 3: 5}
# x.clear()   {}
# print(x.get("abc"))  4
# print(x.items())  ([(1, 1), ('abc', 4), (3, 5)])
# print(x.keys())  ([1, 'abc', 3])
# print(x.values())  ([1, 4, 5])
# print(len(x))  3

# x = {"apple", "banana", "cherry","apple"}
# print(len(x)) 3

# x = {1,2,4,6,8} 

# x.add(5)  {1, 2, 4, 5, 6, 8}
# x.update({10,9})   {1, 2, 4, 6, 8, 9, 10}
# x.discard(4)   {1, 2, 6, 8}
# x.pop()    {2, 4, 6, 8}
# print(x)


# a = 33
# b = 200

# if b <= a:
#     print("b is greater than a")


# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# a = 200
# b = 500

# print("A") if a > b else print ("B")

# if a > b :
#     print("A")
# else:
#     print("B")

# a = 200
# b = 800
# c = 100
# if a > b or c > a:
#   print("Both conditions are True")
# else:
#   print("invalid")

# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")
# else:
#   print("Not")

# x = 41

# if x > 100:
#   print("Above ten,")
#   if x > 50:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
# else:
#   print("not valid")

# a = 33
# b = 200

# if b > a:
#   pass

#   if b > a:
#     print("a")


# i = 0
# while i < 10:
#   print(i)
#   i = i + 1 

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# 1
# 2
# 3

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)   


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for x in "banana":
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)                    ---> apple , banana
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x) <-----apple

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)   ------>apple,cherry

# for x in range(1,6):
#   print(x)     1,2,3,4,5

# for x in range(2, 6):
#   print(x)    2,3,4,5

# for x in range(2, 30, 3):
#   print(x)        2,5,8,11,14,17,20,23,26,29

# for x in range(6):
#   if x == 3: 
#     break
#   print(x)
# else:
#   print("Finally finished!")  012


# n = 5

# for i in range(n):  #column
#     for j in range(i+1) :  #row
#         print(' *',end='')
#     print()  

# *
# * *
# * * *
# * * * *
# * * * * *

# for x in [0, 1, 2]:
#   pass


x = [7, 9, 12, 11, 3]

# for i in range (0,len(x)):
#     for j in range(0,len(x)-1):
#         if x[j] > x[j+1]:
#             x[j],x[j+1] = x[j+1],x[j]

# print(x)


for i in range(0,len(x)):
    min_val = i
    for j in range(i+1,len(x)):
        if x[j] < x[min_val]:
            min_val = j
            x[i],x[min_val]=x[min_val],x[i]
print(x)