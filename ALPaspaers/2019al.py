result = 0
s = input()

if (len(s) > 3):
    result = 2
if (len(s) > 6):
    result = 3
elif (len(s) > 6):
    result= 4
else:
    result = 5
print(result)