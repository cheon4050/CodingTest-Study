import sys

n = int(sys.stdin.readline())
energy = [[0, 0]]
for _ in range(n - 1):
    energy.append(list(map(int, sys.stdin.readline().split())))
k = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    if i == 2:
        dp[i] = dp[i - 1] + energy[i - 1][0]
        continue
    dp[i] = min(dp[i - 1] + energy[i - 1][0], dp[i - 2] + energy[i - 2][1])
result = dp[n]
for i in range(4, n + 1):
    temp = dp[:i] + [0 for _ in range(n - i + 1)]
    temp[i] = temp[i - 3] + k
    for j in range(i + 1, n + 1):
        temp[j] = min(temp[j - 1] + energy[j - 1][0], temp[j - 2] + energy[j - 2][1])
    result = min(result, temp[n])
print(result)