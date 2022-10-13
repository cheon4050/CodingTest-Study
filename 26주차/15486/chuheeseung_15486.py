import sys
input = sys.stdin.readline

n = int(input())
t = [] # 시간
p = [] # 이익
dp = [0] * (n + 1) # 상담을 진행하면 얻을 수 있는 이익을 저장하는 리스트
# 상담이 끝나는 날 위치에 이익이 들어감

for i in range(n):
    temp = list(map(int, input().split()))
    t.append(temp[0])
    p.append(temp[1])

k = 0
for i in range(n):
    k = max(k, dp[i]) # max(이전에 저장된 k값, dp[i])

    if i + t[i] > n: # i번째 날에 상담 시작하면 i+t[i]가 n을 넘지 않아야 한다
        continue

    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])
    # max(현재까지의 수익 + 이번 상담의 수익, 오늘의 상담이 끝나는 시점의 수익)

print(max(dp))