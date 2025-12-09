def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0
    for i in range(len(s)):
        left, right = i-1, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > end - start:
            start, end = left + 1, right - 1
    return s[start:end + 1]

# Example usage:
print(longestPalindrome("babad"))  # Output: "bab" or "aba"
print(longestPalindrome("cbbd"))   # Output: "bb"