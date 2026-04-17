import csv
file=input("enter the file name: ")
fptr=open(file,"a",newline="")
write=csv.writer(fptr)
write.writerow(["Sl No","Name","Age"]) 
n=int(input("enter the number of employees: "))

for i in range(n):
    name=input("enter the employee name: ")
    age=input("enter the employee age: ")
    write.writerow([i+1,name,age]) 

fptr.close()