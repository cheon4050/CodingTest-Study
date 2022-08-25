import sys

stack = []
result = 0
string = list(sys.stdin.readline().rstrip())
for char in string:
    if char == '(':
        stack.append(char)
    else:
        if stack[-1] == '(':
            stack.pop()
            if stack and type(stack[-1]) == int:
                stack[-1] += 1
            elif stack:
                stack.append(1)
        else:
            raser = stack.pop()
            stack.pop()
            result += raser + 1
            if stack:
                if type(stack[-1]) == int:
                    stack[-1] += raser
                else:
                    stack.append(raser)
print(result)