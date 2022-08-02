import sys
input = sys.stdin.readline

word = list(input().rstrip()) # 문자열
x = list(input().rstrip()) # 폭발 문자열
stack = []

for i in word:
    stack.append(i) # 문자열 차례로 스택에 저장

    if stack[-1] == x[-1] and len(stack) >= len(x): # 스택의 마지막 글자랑 문자열의 (i+1)번째 문자열이랑 같은 경우
        if stack[-len(x):] == x: # 폭발 문자열이랑 같은 경우 pop
            for i in range(len(x)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")