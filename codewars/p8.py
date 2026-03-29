def find_average(numbers):
    total=0
    count=0
    if not numbers:
        return 0
    for i in numbers:
        total+=i
        count+=1
    print(total)
    print(count)
    return total/count
find_average([])