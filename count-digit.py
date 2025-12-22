def count_digit(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

ls = [0, 13, 5, 23, 456, 7890, 12345, 678901]
for num in ls:
    print(f"Number: {num}")
    print(f"Digit Count: {count_digit(num)}\n")