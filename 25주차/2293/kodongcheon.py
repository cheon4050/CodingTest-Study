import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0]*(k+1)
dp[0] = 1
arr = [int(input())for i in range(n)]
for A in arr:
    for i in range(A,k+1):
        dp[i] += dp[i-A]
print(dp[k])

