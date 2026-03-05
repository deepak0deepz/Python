def pal(n):
    temp=n
    if n<0:
        n*=-1
    rev=0
    while n>0:
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    if temp<0:
        rev*=-1
    return temp==rev
s1=int(input("starting number"))
s2=int(input("starting number"))
if s1>s2:
    print("s1 shd be smaller")
else:
    print("palidrom")
    for i in range(s1,s2+1):
        flag=pal(i)
        if flag:
            print(i,end=" ")
            
