def rem(s):
    if len(s)<3:
        return ""
    elif len(s)==3:
        return s[1]
    else:
        s1=len(s)
        k=s[1:s1-2]+s[s1-2:s1-1]
        return k
rem("palidorrrrsdfea")