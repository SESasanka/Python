notes=[5000,1000,500,100,50,20,10,5,2,1]
new_notes=[]
total_notes=[0,0,0,0,0,0,0,0,0,0]
total=0
file1=open("input.txt","r")
file2=open("output.txt","w")
line=file1.readline()
while line:
    data=line.strip().split('-')
    sal=int(data[1])
    for x in notes:
        quo=sal//x
        sal=sal%x
        new_notes.append(quo)
    file2.write(f"{data[0]}-\n")
    for i in range(len(notes)):
        if new_notes[i]>0:
           file2.write(f"{notes[i]}X{new_notes[i]}-{notes[i]*new_notes[i]}\n")
           total+=notes[i]*new_notes[i]
           total_notes[i]+=new_notes[i]
    new_notes=[]
    file2.write(f"Total - {total}\n")
    file2.write(f"\n")
    total=0
    line=file1.readline()
file2.write(f"Total notes-\n")
for j in range(len(notes)):
    if total_notes[j]>0:
        file2.write(f"{notes[j]} - {total_notes[j]}\n")
file1.close()
file2.close()
