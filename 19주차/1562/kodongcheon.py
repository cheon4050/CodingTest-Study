import sys
sys.setrecursionlimit(10**8)
N = int(input())
def dfs(cnt,now, visited):
    global result
    if cnt == N-1:
        if visited == (1<<10)-1:
            return 1
        else:
            return 0
    if dp[cnt][now][visited]:
        return dp[cnt][now][visited]
    cost = 0
    if now - 1 >= 0:
        cost += dfs(cnt +1, now - 1, visited | (1 << (now - 1)))
    if now + 1 <= 9:
        cost += dfs(cnt +1, now + 1, visited | (1 << (now + 1)))
    dp[cnt][now][visited] = cost
    return dp[cnt][now][visited]

result = 0
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N)]

for k in range(1,10):
    result += dfs(0, k,1<<k)
print(result%(1000000000))