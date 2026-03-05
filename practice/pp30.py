def lp(n):
    return (n%100!=0 and n%4==0) or(n%400==0)
yearb=int(input("enter the year"))
yeare=int(input("enter the year"))
while yearb<yeare+1:
    flag=lp(yearb)
    if flag:
        print(yearb,end=" ")
    yearb+=1