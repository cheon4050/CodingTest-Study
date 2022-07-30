string = input()
bomb = input()
stack = []
length = len(bomb)

for char in string:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

if len(stack)==0:
    print("FRULA")
else:
    str = ""
    print("".join(stack))
    print(str)