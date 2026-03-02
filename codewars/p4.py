def print_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        print(" " * (n - i)*2 , end=" ")

        for j in range(i):
            print(f"{"*":<5}", end="")
            num += 2
        print()

print_pyramid(5)