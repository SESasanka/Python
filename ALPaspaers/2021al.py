s = 1

for i in range(1,10):
    if i < 5:
        s *= i
    elif i < 8:
        s -= i
    else:
        s += i
        break
print(s)