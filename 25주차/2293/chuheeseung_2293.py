import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)] # 코인의 종류
dp = [0 for i in range(k + 1)] # k+1개 만큼 리스트 선언
dp[0] = 1 # 0번 인덱스는 동전 1개만 쓸 때의 경우의 수를 고려
# dp[k] = 합이 k원이 되는 경우의 수

for i in coin: # 코인의 종류만큼 전부 순회
    for j in range(i, k + 1): # 이부분 이해 못함
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])