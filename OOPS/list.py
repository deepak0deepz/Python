def listt():
    arr=[]
    i=0
    while True:
        n=int(input("enter number :  "))
        arr.insert(i,n)
        i+=1
        c=int(input("1 ---> continue or other to exit"))
        if c==1:
            continue
        else:
            return arr
print(listt())