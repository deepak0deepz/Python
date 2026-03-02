def reverse_words(w1):
    w1=input("enter :")
    w=w1.split(" ")
    s=""
    for i in w:
        s+=i[::-1]+" "
    print(s)
reverse_words("hello world")