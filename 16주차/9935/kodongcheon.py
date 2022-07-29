import sys
input = sys.stdin.readline

s = input().rstrip()
check = list(input().rstrip())
temp = []
check_len = len(check)
for i in s:
    temp += i
    if temp[len(temp)-check_len:] == check:
        for _ in range(check_len):
            temp.pop()
if temp:
    print("".join(temp))
else:
    print("FRULA")