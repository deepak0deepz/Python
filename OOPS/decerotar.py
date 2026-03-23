def print_msg():
    print("hello every one")

def outer(print1):
    print("entering outrt")
    def inner():
        print("entering inner")
        ref=print1
        ref()
        print("leaving inner")
    print("calling inner")
    return inner 

ptr1=print_msg
ptr2=outer(ptr1)
ptr2()
print("pgm end")