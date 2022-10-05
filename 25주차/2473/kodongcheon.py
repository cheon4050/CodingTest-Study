N = int(input())
arr = list(map(int, input().split()))
arr.sort()
minResult = 3000000000

for i in range(N):
    start, end = i+1, N-1
    while start < end:
        result = arr[i]+arr[end]+arr[start]
        if abs(result) < minResult:
            minResult = abs(result)
            resultTuple = (minResult,arr[i],arr[start],arr[end])
        if result > 0:
            end -= 1
        elif result == 0:
            break
        else:
            start+=1

result = resultTuple[1:]

print(*sorted(result))
