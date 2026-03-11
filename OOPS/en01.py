class Book:
    def __init__(self,value):
        self.__pages=value
    def setter(self,value):
        if value>=1:
            self.__pages=value
    def getter(self):
        return self.__pages
b=Book(00)
b.setter(114)
res=b.getter()
print(res)
b.setter(15)
res=b.getter()
print(res)

