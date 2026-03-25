def fun1():
    print("enteringggggggggg")
    try:
        fun2()
    except Exception as e:
        print("error is ",e)
    print("leaving fun1")

def fun2():
    print("entering 2")
    try:
        res=10/0
        print(res)
    except Exception as e:
        print("error is ",e)
        raise e
    print("leaving fun2")
    

print("start")
fun1()
print("end")