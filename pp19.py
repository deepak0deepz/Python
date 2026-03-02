class Farmer:
    r=2.5
    def __init__(self,p,t):
        self.p=p
        self.t=t
    def display(self):
        si=(self.p*self.t*Farmer.r)/100
        print(f"simple interest is : {si}")
f1=Farmer(1000,2)
f1.display()

