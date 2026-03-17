class Heart:
    def __init__(self, name):
        self.hname = name
        print(f"{self.hname} heart is created")

    def getheart(self):
        print("Heart is working")

class Car:
    def __init__(self, name):
        self.cname = name
        print("Car is ready")

    def getCar(self):
        print("Car is running")

class Person:
    def __init__(self, name):
        self.pname = name
        self.heart = Heart("Human")
        self.car = None
        
        print("Person is created")

    def hasCar(self, car_obj):
        self.car = car_obj
        print("Person got a car")

p1 = Person("Deepak")

print(p1.pname)
p1.heart.getheart()

c1 = Car("BMW")
p1.hasCar(c1)

print(p1.car.cname)
p1.car.getCar()