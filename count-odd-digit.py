def countOddDigit(n):
    count = 0
    while n > 0:
        if (n % 10) % 2 != 0:
            count += 1
        n //= 10
    return count

ls = [23, 456, 246, 7890, 12345, 678901]
for num in ls:
    print(f"Number: {num}")
    print(f"Odd Digit Count: {countOddDigit(num)}\n")