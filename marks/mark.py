total_marks = {}
file = open("stmarks.txt", "r")
file2 = open("output.txt", "w")
line = file.readline()
while line:
    data = line.strip().split(",")
    totalMark = int(data[1])+int(data[2])+int(data[3])
    name = data[0]
    total_marks.update({name: totalMark})
    line = file.readline()
file2.write(f"Total marks-\n")
for j in range(len(total_marks)):
    file2.write(f"{total_marks.items()}\n")
file.close()
file2.close()
