exp = input()
stack = []
for e in exp:
    if e.isalpha():
        print(e, end='')
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif e in "+-":
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(e)
    else:
        while stack and stack[-1] in '*/':
            print(stack.pop(), end='')
        stack.append(e)

while stack:
    print(stack.pop(), end='')
