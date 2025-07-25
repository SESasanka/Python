# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


list_a =[5,15,20,16,8]

def f(x):
    total = 0
    for i in x:
        total = total+i
        if total >= 50:
            break
    return (total)
print(f(list_a))