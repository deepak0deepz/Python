def count(n):
    temp=n
    count=0
    if n <0:
        n*=-1
    while n>0:
        n//=10
        count+=1
    return count

def asn(n):
    temp=n
    asn=0
    p=count(n)
    while n >0:
        base=n%10
        asn+=base**p
        n//=10
    return temp==asn
    
k=asn(525)
print(k)