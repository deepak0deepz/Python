class Parents:
    def __init__(self):
        self.a=10
class Child(Parents):
    def __init__(self):
        Parents.__init__(self)      #<---- manually invoking the parent class
        self.b=20
class Son(Child):
    def __init__(self):
        Child.__init__(self)
        self.c=30

cf=Son()
print(cf.a)
print(cf.b)
print(cf.c)