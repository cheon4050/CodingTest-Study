import sys
input = sys.stdin.readline
N = int(input())
s = input().rstrip()

stack = [s[0]]
cnt = 1
for i in range(len(s)):
    if stack and s[i] == "R":
        stack = []
        cnt +=1
    elif s[i] == "B":
        stack.append("B")

stack = [s[0]]
cnt2 = 1
for i in range(len(s)):
    if stack and s[i] == "B":
        stack = []
        cnt2 +=1
    elif s[i] == "R":
        stack.append("R")
print(min(cnt, cnt2))