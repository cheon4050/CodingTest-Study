import sys
input=sys.stdin.readline
string=list(input().rstrip())
bomb=list(input().rstrip())
stack=[]
for s in string:
    stack.append(s)
    if stack[-1]==bomb[-1] and len(stack)>=len(bomb):
        if stack[-len(bomb):]==bomb:
            for _ in range(len(bomb)):
                stack.pop()
print(*stack if stack else "FRULA",sep="")