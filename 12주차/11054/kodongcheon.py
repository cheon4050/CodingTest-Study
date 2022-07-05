import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp = [1] * (N)
dp[0] = 1
for i in range(1,N):
    for j in range(i, -1, -1):
        if arr[j] >= arr[i]:
            continue
        else:
            dp[i] = max(dp[i], dp[j] + 1)

dp2 = [1] * (N)
dp2[-1] = 1
for i in range(N-1,-1,-1):
    for j in range(i,N):
        if arr[j] >= arr[i]:
            continue
        else:
            dp2[i] = max(dp2[i], dp2[j] + 1)

result =0
for i in range(N):
    result = max(result, dp[i]+dp2[i]-1)
print(result)
