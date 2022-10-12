# 필요한 메모리 M 바이트를 확보하기 위한 앱 비활성화의 최소의 비용을 구하기

N, M = map(int, input().split())  # 앱 개수, 필요한 바이트 수
arr = [[0, 0] for _ in range(N + 1)]
m_lis = list(map(int, input().split()))  # 활성화 앱 사용중인 메모리 바이트 수
c_lis = list(map(int, input().split()))  # 비활성화 앱을 다시 활성화 했을 때 비용
cost = sum(c_lis)
dp = [[0] * (cost + 1) for _ in range(N + 1)]  # dp[i][j]: i번째 앱까지 중 j 코스트로 얻을 수 있는 최대의 byte

for i in range(N):
    arr[i+1][0] = m_lis[i]
    arr[i+1][1] = c_lis[i]

result = float("inf")
for i in range(1, N + 1):
    m, c = arr[i][0], arr[i][1]

    for j in range(1, cost + 1):
        if j < c:     # 현재 앱을 비 활성화 할 만큼의 cost가 충분하지 않은 경우
            dp[i][j] = dp[i - 1][j]  # 앱 활성화
        else:         # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + m)

        if dp[i][j] >= M:
            result = min(result, j)    # 최소 비용
print(result)
