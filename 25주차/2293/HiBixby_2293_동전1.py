n, k = map(int, input().split())
# 동전 종류 입력
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
# 경우의 수 계산
number_of_cases = [0]*(n+1)
for index, number in enumerate(number_of_cases):
    if index<coins[0]:
        continue
    for coin in coins:
        

# 점화식
# dp[i] = dp[i-coin] + 