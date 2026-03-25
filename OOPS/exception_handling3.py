def fun1(a,b):
    print(b/a)

try:
    a=int(input("num 1 : "))
    b=int(input("num 2 : "))
    fun1(a,b)
except Exception as e:
    print(e.__str__())
else:
    print("went good without error")
finally:
    print("pgm end")
    