def c(arr):
    count=0
    total=0
    if not arr:
        return []
    for i in arr:
        if i>0:
            count+=1
        if i<0:
            total+=i
    return [count,total]
c([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])