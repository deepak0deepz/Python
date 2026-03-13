class Plane:
    def takeoff(self):
        print("plane is takeoff")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class Cargo(Plane):
    def carryg(self):
        print("plane carry goods")

class Passenger(Plane):
    def carryp(self):
        print("plane carry passenger")

class Fighter(Plane):
    def carryw(self):
        print("plane carry weapons")
        
c=Cargo()
p=Passenger()
f=Fighter()

c.takeoff()
c.fly()
c.land()
c.carryg()

p.takeoff()
p.fly()
p.land()
p.carryp()

f.takeoff()
f.fly()
f.land()
f.carryw()