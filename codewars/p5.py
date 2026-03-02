def i(s):
    s1=s.split(" ")
    strr=""  
    for i in s1:
        if i:
            strr+=i[0].upper()+i[1:].lower()+" "
        else:
            strr+=" "
    return strr
        
print(i("How can mirrorsSSSS be real if our eyes aren't real"))