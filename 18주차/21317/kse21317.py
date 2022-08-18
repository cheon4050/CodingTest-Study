#징검다리 건너기
# dp[0][n] : 매우 큰 점프 x, n번째 돌까지 소비한 에너지
# dp[1][n] : 매우 큰 점프 o, n번째 돌까지 소비한 에너지
N = int(input())
small = []
big = []
for _ in range(N-1):
    s, b = map(int, input().split())
    small.append(s)
    big.append(b)
mega = int(input())

if N >= 4:
    dp = [[0] * (N+1) for _ in range(2)]

    dp[0][2] = small[0]
    dp[0][3] = min(dp[0][2] + small[1], big[0])
    dp[1][4] = mega

    for i in range(4, N+1):
        dp[0][i] = min(dp[0][i-2]+big[i-3], dp[0][i-1]+small[i-2])

        if i == 4:
            continue

        if i >= 5:
            dp[1][i] = min(dp[0][i-3]+mega ,dp[1][i-1]+small[i-2])
        if i >= 6:
            dp[1][i] = min(dp[1][i] ,dp[1][i-2]+big[i-3])

    print(min(dp[0][N], dp[1][N]))
elif N == 3:
    print(min(small[0] + small[1], big[0]))
elif N == 2:
    print(small[0])
elif N == 1:
    print(0)