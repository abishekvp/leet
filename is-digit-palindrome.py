def isPalindrome(n):
    out = 0
    num = n
    while n:
        out = (out * 10) + (n % 10)
        n //= 10
    return True if num < 10 else out == num

ls = [121, 494, 12321, 123, 45654, 78987, 1234321, 10]
for num in ls:
    print(f"Number: {num}")
    print(f"Is Palindrome: {isPalindrome(num)}\n")