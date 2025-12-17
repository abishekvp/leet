def pattern18(n):
    # Get the ASCII value of the first character we need (e.g., 'E' for n=5)
    # ord('A') is 65. For n=5, start_char is 69 ('E')
    for i in range(1, n + 1):
        # The starting letter for each row shifts back one by one
        start_val = ord('A') + n - i
        for j in range(i):
            # We print from the starting letter up to the Nth letter
            print(chr(start_val + j), end=" ")
        print()

pattern18(5)