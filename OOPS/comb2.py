class Heart:
    def __init__(self,name):
        self.hname=name
        print(f"{self.hname} is person ")
    def getheart(self):
        print("heart xyz")

class Car:
    def __init__(self,name):
        self.cname=name
        print("car ready")
    def getCar(self):
        print("drive it")

class Person:
    def __init__(self,name):
        self.pname=name
        self.heart=Heart("human")
        self.c1=None
    def hasPerson(self,c):
        self.c1=c

p1=Person("DEEPAK")
c1=Car("toyota")
p1.hasPerson(c1)
print(p1.pname)
print(c1.cname)

