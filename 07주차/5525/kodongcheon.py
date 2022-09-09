import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

s = list(input().rstrip())

stack = []
cnt = 0
result = 0
for i in s:
    if not stack:
        if i == "I":
            stack.append(i)
            cnt+=1
            continue
        continue
    if i != stack[-1]:
        stack.append(i)
        cnt+=1
    else:
        temp = (cnt-(2*(N-1)+1)) // 2
        if temp >0:
            result += temp
        if i == "I":
            stack = [i]
            cnt = 1
        else:
            stack = []
            cnt = 0
if cnt >= 0:
    temp = (cnt - (2 * (N - 1) + 1)) // 2
    if temp > 0:
        result += temp
print(result)


