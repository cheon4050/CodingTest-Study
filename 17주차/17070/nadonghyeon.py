import sys

input = sys.stdin.readline

n = int(input())
# G = [list(map(int,input().split())) for _ in range(n)]

G = [[0 for _ in range(n)]]
for _ in range(n):
    G.append(list(map(int,input().split())))
dp = [[[0,0,0] for _ in range(n)] for _ in range(n+1)] # 가로 대각선 세로

dp[1][1] = [1,0,0]


for i in range(1,n+1):
    for j in range(1,n):
        if i==j==1:
            continue
        if G[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1] # 가로
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2] # 세로
            if G[i][j-1] == G[i-1][j] == 0 :
                dp[i][j][1] = sum(dp[i-1][j-1]) # 대각선



print(sum(dp[-1][-1]))