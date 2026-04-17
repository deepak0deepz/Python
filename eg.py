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

s=Student("Deepak", 22, 5.8, "Bengaluruu")
f=open("names.txt","wb")
pickle.dump(s, f)
print("Done")
f.close()
