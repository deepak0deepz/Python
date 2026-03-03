class Demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp
x=int(input("enter the value of a :"))
y=int(input("enter the value of b :"))
d=Demo(x,y)
print(f"before swap a :{d.a} and b :{d.b}")
d.swap()
print(f"after swap a :{d.a} and b :{d.b}")
