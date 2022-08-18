n = int(input()) # 돌의 개수 n
jump = [[0] * 2 for _ in range(n - 1)]
dp = [0] * n

for i in range(n - 1):
    a, b = map(int, input().split()) # 작은 점프 에너지 a, 큰 점프 에너지 b
    jump[i][0] = a # 리스트에 저장
    jump[i][1] = b

k = int(input()) # 매우 큰 점프 에너지 k

if n == 1: # 첫번째 돌에서부터 출발
    print(0)
    exit()
elif n == 2: # 작은 점프로 한번 뛰면 되니까 바로 출력
    print(jump[0][0])
    exit()

dp[1] = jump[0][0] # 1번 돌로 갈 수 있는 방법 : 작은 점프
dp[2] = min(jump[0][0] + jump[1][0], jump[0][1])
# 2번 돌로 갈 수 있는 방법 : 최솟값(1번으로 작은 점프 + 2번으로 작은 점프, 2번으로 큰 점프)

for i in range(3, n): # 3번째 돌 ~ n번째 돌까지는 점화식으로 계산
    dp[i] = min(dp[i-1] + jump[i - 1][0], dp[i - 2] + jump[i - 2][1])
    # 최솟값(전돌 가는 방법 + 전돌에서 작은 점프, 전전돌을 가는 방법 + 전전돌 점프 중 작은 값)

result = dp[-1]
_dp = dp[:] # 새로운 값을 계산하기 위한 dp의 복사본

for i in range(0, n-3):
    if dp[i] + k < dp[i+3]: # i에서 매우 큰 점프한 게 원래 값 dp[i+3]보다 작은 경우
        _dp[i + 3] = dp[i] + k # 새로운 dp를 계산

        for j in range(i + 4, n):
            _dp[j] = min(dp[j], _dp[j - 1] + jump[j - 1][0], _dp[j - 2] + jump[j - 2][1])
            # 원래 값과 이전에 비교한 값 중 최솟값

        if _dp[-1] < result:
            result = _dp[-1]

print(result)