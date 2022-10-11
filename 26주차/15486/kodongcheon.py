import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
dp = [0] * (N+50)
dp[arr[0][0]] = arr[0][1]
maxCnt = 0
for i in range(1,N):
    maxCnt = max(maxCnt, dp[i])
    dp[i+arr[i][0]] = max(dp[i+arr[i][0]], maxCnt+arr[i][1])
print(max(dp[:N+1]))
