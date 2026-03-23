class A:
    def show(self):
        print("Class A")
print(A.mro())
class B:
    def show(self):
        print("Class B")
print(B.mro())
class C(A,B):
    def show(self):
        print("class C")
print(C.mro())