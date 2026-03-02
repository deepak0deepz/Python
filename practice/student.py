class Student:
    def __init__(self,name,usn,mail,contact):
        self.name=name
        self.usn=usn
        self.mail=mail 
        self.contact=contact 
    def disp(self):
        print(f"\nstudent name: {self.name} \nstudent usn: {self.usn} \nstudent mail: {self.mail} \nstudent contact number: {self.contact}")
n1=input("enter name : ")
n2=input(f"{n1} enter usn number : ")
n3=input(f"{n1} enter the mail: ")
n4=int(input(f"{n1} enter the mobile number : "))
s=Student(n1,n2,n3,n4)
s.disp()

