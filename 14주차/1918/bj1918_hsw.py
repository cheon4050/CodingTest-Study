import sys

equation = sys.stdin.readline().rstrip()
stack = []
result = []
for char in equation:
    if char.isalpha():
        result.append(char)
    else:
        if char == '(':
            stack.append(char)
        elif char == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if char in '-+':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.append(char)
            else:
                while stack and stack[-1] in '*/':
                    result.append(stack.pop())
                stack.append(char)
while stack:
    result.append(stack.pop())
print(''.join(result))