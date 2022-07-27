import sys
input = sys.stdin.readline
N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
for i in range(N):
    max_temp = max_dp[:]
    min_temp = min_dp[:]
    a, b, c = map(int, input().split())
    max_dp[0] = max(max_temp[0], max_temp[1]) + a
    max_dp[1] = max(max_temp) + b
    max_dp[2] = max(max_temp[1], max_temp[2]) + c
    min_dp[0] = min(min_temp[0], min_temp[1]) + a
    min_dp[1] = min(min_temp) + b
    min_dp[2] = min(min_temp[1], min_temp[2]) + c
print(max(max_dp), min(min_dp))