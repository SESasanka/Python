total_marks={}
file = open("stmarks.txt","r")
line = file.readline()
while line:
    data = line.strip().split(",")
    totalMark = int(data[1])+int(data[2])+int(data[3])
    name = data[0]
    total_marks.update({name:totalMark})
    line=file.readline()
print(total_marks)
file.close()
