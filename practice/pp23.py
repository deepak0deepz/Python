def check(n):
    if n % 2 == 0:
        print(f"The number {n} is Even.")
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = check(num)
k=result
print("-")
print(len(k))