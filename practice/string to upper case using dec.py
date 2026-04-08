#WAP to  convert from string to upper case by using decoratore in python
def print_msg():
    msg="deepak"
    return msg
def outer(print1):
    print("entering outer")
    def inner():
        print("inside inner")
        ref=print1
        res=ref()
        res1=res.upper()
        print(res1)
        print("leaving inner")
    return inner
ptr1=outer(print_msg)
ptr1()
print("pgm end")
