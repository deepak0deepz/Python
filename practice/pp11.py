data=input()
newstr=""
i=0
while (i<=len(data)-1):
    datach=data[i]
    asi=ord(datach)
    if 65<=asi<=90:
        x=asi+32
        chrar=chr(x)
    else:
        chrar=datach
    newstr+=chrar
    i+=1
print(newstr)