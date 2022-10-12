N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)   # dp[n] = n일째 까지의 상담 최대 번 금액(이익)

max_val = 0
for i in range(N):
    t, p = arr[i][0], arr[i][1]
    max_val = max(max_val, dp[i])    # 큰 값 갱신

    if i + t > N:      # N+1일에는 회사에 없어서 일을 하지 못함
        continue

    dp[i+t] = max(max_val + p, dp[i+t])  # max( 현재 까지 수익 + 이번 상담의 수익, 오늘의 상담이 끝나는 시점의 수익)
print(max(dp))


