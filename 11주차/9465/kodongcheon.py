T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(max(int(input()), int(input())))
        continue
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[0]*(N) for i in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    for i in range(2,N):
        for j in range(2):
            dp[j][i] = max(dp[1-j][i-1],dp[1-j][i-2],dp[j][i-2]) + arr[j][i]
    print(max(dp[0][-1],dp[1][-1]))