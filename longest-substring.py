
def longest_substring(s):
    temp = ""
    chunk = []
    out = 0
    for i in s:
        if i in temp:
            chunk.append(temp)
            temp = i
        else:
            temp += i
    chunk.append(temp)
    for i in chunk:
        if len(i) > out:
            out = len(i)
    return out

s = ["abcabcbb", "bbbbb", "pwwkew", "abcd", "aab", "abba", ""]
out = [3, 1, 3, 4, 2, 2, 0]
for i in range(len(s)):
    print(longest_substring(s[i])==out[i])