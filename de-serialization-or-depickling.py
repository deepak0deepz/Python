import pickle
class Student:
    def __init__(self, name, age,height,address):
        self.name = name
        self.age = age
        self.height = height
        self.address = address
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Height: ", self.height)
        print("Address: ", self.address)

f=open("names.txt","rb")
s=pickle.load(f)
s.display()
print("done")
f.close()
