def fibb(n):
    n1,n2=0,1
    l=[]
    while n>0:
        print(n1,end=" ")
        l.insert(0,n1)
        add=n1+n2
        n1=n2
        n2=add
        n-=1
    print()
    return l 
n=int(input("enter the range to get the series: "))
print(fibb(n))