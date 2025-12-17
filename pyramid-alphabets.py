def pattern17(n):
    char_code = ord('A')
    for i in range(n):
        print(" " * (n - i -1), end="")
        for j in range(i+1):
            print(chr(char_code + j), end="")
        for j in range(i-1, -1, -1):
            print(chr(char_code + j), end="")
        print()

pattern17(5)