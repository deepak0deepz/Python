class charger:
    def __init__(self,name):
        self.cname=name
        print("charger is ready")
    def getcharger(self):
        print("charger is using to charge")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.c1=""
        print("mobile is ready")
    def hasmob(self,c):
        self.c1=c
        print("both ch and mob us connected")
m=Mobile("vivo")
ch=charger("ctype")
m.hasmob(ch)
print(m.mname)
print(m.c1.cname)
