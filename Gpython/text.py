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


mylist = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(len(mylist)):
  for j in range(len(mylist)-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]  

print(mylist)