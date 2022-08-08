s = input().rstrip()

maxResult = ""
minResult = ""
stack = []

for i in s:
    if i == "M":
        stack.append(i)
    else:
        if not stack:
            maxResult += "5"
            minResult += "5"
        else:
            maxResult += "5" + "0"*len(stack)
            minResult += "1" + "0"*(len(stack)-1)
            minResult += "5"
            stack = []
if stack:
    maxResult += "1" * len(stack)
    minResult += "1" + "0" * (len(stack) - 1)
print(int(maxResult))
print(int(minResult))