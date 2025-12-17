def print_pattern(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            bottom = (size - 1) - i
            right = (size - 1) - j
            current_val = n - min(top, bottom, left, right)
            print(current_val, end=' ')
        print()

print_pattern(6)