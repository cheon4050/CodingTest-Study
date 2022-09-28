import sys
sys.setrecursionlimit(10**6)
arr = list(map(int, input().split()))
arr.pop()
countArr = [[0] * 5 for i in range(5)]
for i in range(5):
    countArr[i][i] = 1
countArr[0][1], countArr[0][2], countArr[0][3], countArr[0][4] = 2, 2, 2, 2
countArr[1][2], countArr[1][3], countArr[1][4] = 3, 4, 3
countArr[2][1], countArr[2][3], countArr[2][4] = 3, 3, 4
countArr[3][1], countArr[3][2], countArr[3][4] = 4, 3, 3
countArr[4][1], countArr[4][2], countArr[4][3] = 3, 4, 3

def solve(n, l, r):
    global dp
    if n>= len(arr):
        return 0
    if dp[n][l][r] != -1:
        return dp[n][l][r]

    dp[n][l][r] = min(solve(n+1, arr[n], r)+countArr[l][arr[n]], solve(n+1, l, arr[n])+countArr[r][arr[n]])
    return dp[n][l][r]

dp = [[[-1]*5 for _ in range(5)]for _ in range(100000)]
print(solve(0, 0, 0))
