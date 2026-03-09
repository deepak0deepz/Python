def reccountnum(n,count=0):
    if n<=0:
        return count
    n//=10
    count+=1
    return reccountnum(n,count)
n=int(input("enter the number to check count of it"))
print(f"the count of {n} is",reccountnum(n))