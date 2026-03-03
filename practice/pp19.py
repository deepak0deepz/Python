class Demo:
    a=10                                                  #<----static variable
    def __init__(self):
        self.b=20
        self.c=21
    def instanceDisp(self):                               #<----instance method
        print(f"the value of b :{self.b} and c :{self.c} ")
    @staticmethod
    def staticDisp():                                      #<----static method
        print(f"the value of a is :{Demo.a}")
    @classmethod
    def classDisp(cls):                                   #<----class  method
        print("the value os a b c is above") 
d=Demo()
d.instanceDisp()
Demo.staticDisp()
Demo.classDisp()  