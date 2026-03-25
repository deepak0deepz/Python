def fun1():
    print("enteringggggggggg")
    try:
        fun2()
    except Exception as e:
        print(print("error is "))
    print("leaving fun1")

def fun2():
    print("entering 2")
    res=10/0
    print(res)
    print("leaving fun2")

print("start")
fun1()
print("end")