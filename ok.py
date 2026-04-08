from itertools import zip_longest
pnames=["kohli","dhoni","iyer","pandya"]
jnum=[18,7,96,33]
runs=[8500,5000,3000,6000]
team=["rcb","csk"]

for i in zip_longest (pnames,jnum,runs,team,fillvalue="#"):
    print(i)
print()

res=list(zip_longest(pnames,jnum,runs,team,fillvalue="-"))
print(res)

