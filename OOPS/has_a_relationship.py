class Radio:
    def turnon(self,x):
        if x==1:
            print("yes radio is on")
        else:
            print("no it is still off")
class Car:
    def __init__(self,min,max):
        self.min=min
        self.max=max
        self.r=Radio()
        self.diff=max-min
x=int(input("min: "))
y=int(input("max: "))
z=int(input("radio: "))
c=Car(x,y)
print(c.min)
print(c.max)
print(f"the diff is {c.max} & {c.min} : ->>> ",c.diff)
c.r.turnon(z)  