#wap to collect only 5 int value elements and store it in a list format
l=[]
for i in range(5):
    a=int(input("Enter the value: "))
    l.append(a)
print(l)

#WAP TO COLLECT FIVE INT VALUE FROM USER AND PRINT ONLY EVEN NUMBERS FROM ELEMENT
l=[]
e=[]
n=input("enter the range :")
for i in range(int(n)):
    a=int(input("Enter the value:"))
    l.append(a)
for i in l:
    if i%2==0:
        e.append(i)
print(l)
print(e)