import csv

file = input("enter the file name: ")
fptr = open(file, "r")
read = csv.reader(fptr)

for row in read:
    print(row)

fptr.close()