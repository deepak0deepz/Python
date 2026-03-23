class Student:
    def __init__(self, name):
        self.name = name

class Usn(Student):
    def __init__(self, name, usn):
        super().__init__(name)
        self.usn = usn

    def Disp(self):
        print(f"{self.name} usn is {self.usn}")

u = Usn("dcs", "012")
u.Disp()