import sys
input = sys.stdin.readline
N = int(input())
s = []
m = []
for _ in range(N-1):
    a, b = map(int, input().split())
    s.append(a)
    m.append(b)
K = int(input())

result = []
for t in range(N-1):
    dp = [int(1e9)] * (N + 2)
    dp[0] = 0
    for i in range(N-1):
        if i == t:
            dp[i+3] = min(dp[i+3], dp[i]+K)
        dp[i+1] = min(dp[i+1], dp[i]+s[i])
        dp[i+2] = min(dp[i+2], dp[i]+m[i])
        result.append(dp[N-1])
if N == 1:
    print(0)
else:
    print(min(result))

