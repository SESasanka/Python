x=[5,8,7,2,4]

for i in range(0,len(x)):
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            x[j],x[j+1]=x[j+1],x[j] 
print(x[0])