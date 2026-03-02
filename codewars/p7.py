def f(sq):
    sr=int(sq**0.5)
    if sq==(sr**2):
        sr+=1
        return int(sr**2)
    else:
        return -1
f(25)