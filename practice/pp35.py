z=ord("a")-ord("A")
print(ord("_"),z)
def clear(n):
    string=""
    for i in n:
        asc=ord(i)
        if i ==" ":
            string+=""
        elif i=="_":
            string+="_"
        elif ord("A")<=asc<=ord("Z"):
            asc+=z
            str1=chr(asc)
            string+=str1
        else:
            string+=i
    return string
x=input("enter the name to convert to lower case:")
check=clear(x)
print(check)