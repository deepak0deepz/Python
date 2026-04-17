a=100
b=200
print(c:=a+b)
print(d:=a-b)
print(e:=a*b)
print(f:=a/b)

import time
class Demo:
    def print_msg(self):
        names=["D","e","e","p","a","k"]
        for i in names:
            print(i)
            time.sleep(1)
    
    def print_num(self):
        for i in range(100):
            print(i*i)
            time.sleep(0.2)
s=Demo()
# s.print_msg()
print()
s.print_num()
