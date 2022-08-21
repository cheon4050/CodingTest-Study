s = input()
stack = 0
result = 0
for i in range(len(s)):
    if s[i] == "(":
        stack += 1
    else:
        stack -= 1
        if s[i-1] == ")":
            result += 1
        else:
            result += stack
print(result)


