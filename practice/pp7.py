student=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    student.append([name,score])
marks_list=[]
for m in student:
    marks_list.append(m[1]) 
marks_list=sorted(set(marks_list))
s2score=marks_list[1]
s2name=[]
for n in student:
    if n[1]==s2score:
        s2name.append(n[0])
s2name.sort()
for k in s2name:
    print(k)