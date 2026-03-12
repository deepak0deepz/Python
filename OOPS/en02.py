class Person:
    def __init__(self, name="", age="", usn=""):
        self.name = name
        self.age = age
        self.__usn = usn

    def get_usn(self):
        return self.__usn

    def set_usn(self, usn):
        self.__usn = usn

    usnn = property(get_usn, set_usn)

    def display(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")
        print(f"The usn is {self.__usn}")


d = Person("dcs", 21)
d.usnn = "012"      # setter
print(d.usnn)       # getter
d.display()