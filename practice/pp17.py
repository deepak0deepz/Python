class Demo:
    def disp(self,x,y): #<-----formal parameters
        temp=x
        x=y
        y=temp
        print(f"before x={temp}, y={x}")
        print(f"after x={x}, y={y}")
d=Demo()
x=5
y=7
print(f"Before swapping the value of x={x} y={y}")
d.disp(x,y) #<-----actual parameters
print(f"after swapping the value of x={x} y={y}")