class Vehicle:
    def __init__(self,name):
        self.name=name
    def start(self):
        print(f"the {self.name} vehicle started")
    def stop(self):
        print(f"the {self.name} vehicle stopped")

class Car(Vehicle):
    def __init__(self,name,fuel,vtype):
        super().__init__(name)
        self.fuel=fuel
        self.vtype=vtype
    def displayit(self):
        print(f"the vehicle {self.name} has {self.fuel} {self.vtype} ")
vv=Vehicle("bajaj")
v2=Car(vv.name,"petrol","2wheeler")
v2.displayit()
vv.start()
vv.stop()    