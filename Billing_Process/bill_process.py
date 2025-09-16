name=[]
q=[]
total=[]
def check_items():
    val_item=False
    while True:
        item=int(input("Enter item id -"))
        file1=open("inventory.txt","r")
        line=file1.readline()
        while line:
            data=line.strip().split("-")
            inv_item=int(data[0])
            if inv_item==item:
                val_item=True
            line=file1.readline()
        file1.close()
        if item==-1:
            break
        if val_item==False:
            print("Invalied ID!!!")
            continue
        qty=int(input("Enter quantity -"))
        val_item=False
        bill_process(item,qty)
        
def bill_process(it,qt):
    file1=open("inventory.txt","r")
    line=file1.readline()
    while line:
        data=line.strip().split("-")
        if it==int(data[0]):
            price=int(data[2])*qt
            name.append(data[1])
            q.append(qt)
            total.append(price)
        line=file1.readline()  
    file1.close()

def print_bill():
    gtot=0
    file2=open("bill.txt","w")
    file2.write("--------------------\n")
    file2.write("----Fruits Lanka----\n")
    file2.write("--------------------\n")
    file2.write("Item      qty  Total\n")
    file2.write("--------------------\n")
    for x in range(len(name)):
        file2.write(f"{name[x]:<10}{q[x]:^4}{total[x]:>6}\n")
        gtot+=total[x]
    file2.write("--------------------\n")
    file2.write(f"Total         {gtot:>6}\n")
    file2.write("--------------------\n")
    file2.write("     Thank You      \n")
    file2.write("--------------------\n")
    file2.close()
    
check_items()        
print_bill()
