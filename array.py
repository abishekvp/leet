def getOut(arr):
    great = ""
    mini = ""
    for i in arr:
        if len(i) > len(great):
            great = i
    for i in arr:
        if len(i) >= len(mini) and len(i) < len(great):
            mini = i
    return mini

arr = ["coder", "lkjh", "code"]
print(getOut(arr))

arr = ["abc", "lkjhg", "oiuth", "z"]
print(getOut(arr))