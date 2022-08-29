from collections import defaultdict

N, K = map(int, input().split())

arr = list(map(int,input().split()))
arrDict = defaultdict(int)
arrDict[arr[0]] = 1
start, end = 0, 1
cnt = 1
result = 0
while end < N:
    arrDict[arr[end]] += 1
    cnt += 1
    if arrDict[arr[end]] > K:
        while arrDict[arr[start]] != K+1:
            arrDict[arr[start]] -= 1
            start += 1
            cnt -= 1
        arrDict[arr[start]] -= 1
        start += 1
        cnt -= 1
    else:
        result = max(result, cnt)
    end+=1
print(result)

