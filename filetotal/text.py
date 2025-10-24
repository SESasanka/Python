file = open("nameMark.txt","r")
file1 = open("output.txt","w")

line = file.readline()

while line:
    data = line.strip().split(",")
    total = int(data[1]) + int(data[2])
    file1.write(f'{data[0]}-{total}\n')
    line=file.readline()
file.close()
file1.close()
