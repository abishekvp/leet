def print_butterfly(n):
    # Top Half (including the middle line)
    for i in range(1, n + 1):
        # Left stars
        print("*" * i, end="")
        # Middle spaces
        print(" " * (2 * (n - i)), end="")
        # Right stars
        print("*" * i)

    # Bottom Half
    for i in range(n - 1, 0, -1):
        # Left stars
        print("*" * i, end="")
        # Middle spaces
        print(" " * (2 * (n - i)), end="")
        # Right stars
        print("*" * i)

print_butterfly(5)