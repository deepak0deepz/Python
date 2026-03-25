def fun1():
    print(100/0)
try:
    fun1()
except Exception as e:
    print(e)