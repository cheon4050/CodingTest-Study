n, k = map(int, input().split())
# 동전 종류 입력
coins = [int(input())for _ in range(n)]
# 경우의 수 계산
number_of_cases = [1]+[0]*k
for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0:
            number_of_cases[i] += number_of_cases[i-coin]
print(number_of_cases[k])

# 점화식
# dp[i] += dp[i-coin]
