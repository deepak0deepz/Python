d={
    1:11,
    2:22,
    3:33
}
print("d before modification")
d1=d  
print("d",d)                                             #!  shallow copy
print("d1",d1)
d[1]=110
print("after modification")
print("d",d)                                            
print("d1",d1)

d2=d.copy()                                              #! Deep copy
print(" before modification")
print("d",d)
print("d2",d2)
d[2]=2020
print("After modification")
print("d",d)
print("d2",d2)