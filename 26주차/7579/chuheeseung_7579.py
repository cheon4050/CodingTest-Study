import sys

n, m = map(int, input().split())
memories = list(map(int, input().split()))
cost = list(map(int, input().split()))
tc = sum(cost)
result = sys.maxsize

dp = [[0 for _ in range(tc + 1)] for _ in range(n + 1)]
# dp[i][j] : i번째 앱까지 비용 j로 얻을 수 있는 최대 메모리

for i in range(n):
    for j in range(tc):
        if cost[i] > j: # cost[i]가 j보다 비용이 크면 종료하지 못하니까 이전 값을 그대로 가져와서 넣는다
            dp[i][j] = dp[i-1][j]
        else: # j보다 비용이 작으면 종료 가능 -> 종료 X, O 최댓값을 비교해서 넣는다
            dp[i][j] = max(dp[i-1][j], memories[i] + dp[i-1][j-cost[i]])

        if dp[i][j] >= m: # 현재 비용 j와 이전 result 비교 -> 최솟값 선택
            result = min(result , j)

if m == 0:
    print(0)
elif n == 1:
    print(cost[0])
elif result == sys.maxsize:
    print(n * m)
else:
    print(result)