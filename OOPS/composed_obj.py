class OS:
    def __init__(self):
        self.status=True
        print("OS is installing")
    def getos(self):
        print("os is still installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("mobile object created")
        print("with os is installed")
m=Mobile("vivo")
print(m.mname)
print(m.o.status)
m.o.getos()
# del m    #<<<<<<<--------comment this to run code 
print("after deleted")
print(m.mname)
print(m.o.status)

