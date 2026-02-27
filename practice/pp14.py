s = input()
if s.isalpha():
    print("only alphabet")
elif s.isnumeric():
    print("only number")
elif s.isalnum():
    print("both alphabet & number")
else:
    print("contains special characters")
    