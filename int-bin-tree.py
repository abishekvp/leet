def pattern11(n):
    for i in range(1, n+1):
        f = 0 if (i % 2) == 0 else 1
        for j in range(i):
            print(f, end="")
            f = 0 if f == 1 else 1
        print()

pattern11(5)