N = int(input())

arr = list(map(int, input().split()))
sumArr1 = [arr[0]]
for i in range(1,N):
    sumArr1.append(arr[i]+sumArr1[-1])
sumArr2 = [arr[-1]]
for i in range(N-2, -1, -1):
    sumArr2.append(arr[i]+sumArr2[-1])
result = 0
for i in range(1, N-1):
    result = max(result, sumArr1[i]+sumArr2[N-i-1]-arr[0]-arr[-1])
    result = max(result, 2*sumArr1[-1]-arr[0]-arr[i]-sumArr1[i])
    result = max(result, 2*sumArr2[-1]-arr[-1]-arr[N-1-i]-sumArr2[i])

print(result)