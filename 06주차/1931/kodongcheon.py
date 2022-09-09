import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start,end))

arr.sort(key = lambda x : (x[0], x[1]))
end = 1000000
count = 1

for s in arr:
    if s[0] >= end:
        count+=1
        end = s[1]
    else:
        if s[1] < end:
            end = s[1]
print(count)

