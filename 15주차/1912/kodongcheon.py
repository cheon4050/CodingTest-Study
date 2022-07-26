N = int(input())
arr = list(map(int, input().split()))

cnt = 0
result = 0

for num in arr:
    if cnt + num < 0:
        result = max(cnt, result)
        cnt = 0
    else:
        cnt += num
        result = max(cnt, result)
if result == 0:
    result = max(arr)
print(result)
