
def fn():
    global a
    a=100
    print(a)
    b=20
    print(b)
def fn1():
    global a
    a=1000
    print(a)
    c=30
    print(c)

fn()
print(a)
fn1() 
print(a)