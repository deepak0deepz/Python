def outer():
    print("inside")
    def inner():
        print("inside inner")
    return inner
k=outer()
print(k)
k()
