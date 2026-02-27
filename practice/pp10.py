data=input("enter value: ")
new=""
for c in data:
    cai=ord(c)
    if 65<=cai<=90:
        cai+=32
        corg=chr(cai)
    else:
        corg=c
    new+=corg
print(new)
