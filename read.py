 #: eg1
print("enter the file name: ")
fname=input()
fptr=open(fname,"r")
data1=fptr.read()               #! read() : it reads the entire file and returns it as a string.
print(data1)

 #: eg2

print("enter the file name: ")
fname=input()
fptr=open(fname,"r")
data1=fptr.read(10)              #! read(10) : it reads the first 10 characters from the file.
print(data1)

 #: eg2

print("enter the file name: ")
fname=input()
fptr=open(fname,"r")
data1=fptr.readline()           #! readline() : it reads the first line from the file and returns it as a string.
print(data1)

 #: eg2

print("enter the file name: ")
fname=input()
fptr=open(fname,"r")
data1=fptr.readlines()          #! readlines() : it reads all the lines from the file and returns them as a list of strings.
print(data1)