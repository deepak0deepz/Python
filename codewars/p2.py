def count1(s):
    count=0
    s=s.lower()
    for i in s:
        if i in "aeiou":
            count+=1
    return count
count1("aeiooiiiu")