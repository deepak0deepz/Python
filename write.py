# write 5 employee details in a new employee file using classic write method like ,sl no ,name,age.
# using :>5 to align the text to the right with a width of 5 characters.


fname=input("enter the file name: ")
n=int(input("enter the number of employees: "))
fptr=open(fname,"a")    # w -> write , a -> append, r -> read , b -> binary mode , t -> text mode,
for i in range(n):
    print("enter the employee name: ")
    name=input()
    print("enter the employee age: ")
    age=input()
    fptr.write(f"{i+1}. {name: <6} {age: <5}\n") # using :>5 to align the text to the right with a width of 5 characters.fstring
fptr.close()

