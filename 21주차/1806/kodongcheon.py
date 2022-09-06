import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0

result = 100001
total = 0
while end != N:
    total += arr[end]
    if total >= S:
        while total >= S and start<=end:
            result = min(result, end - start + 1)
            total-=arr[start]
            start +=1
    end += 1
if result == 100001:
    print(0)
else:
    print(result)