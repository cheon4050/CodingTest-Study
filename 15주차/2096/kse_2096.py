n = int(input())
line = []
max_dp=[0,0,0]
min_dp=[0,0,0]

for i in range(n):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    temp = [0, 0, 0]

    temp[0] = max(max_dp[0],max_dp[1]) +a
    temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + b
    temp[2] = max(max_dp[1], max_dp[2]) + c

    max_dp[0],max_dp[1],max_dp[2]=temp[0],temp[1],temp[2]

    temp[0] = min(min_dp[0],min_dp[1]) +a
    temp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + b
    temp[2] = min(min_dp[1],min_dp[2]) +c

    min_dp[0],min_dp[1],min_dp[2]=temp[0],temp[1],temp[2]

print(max(max_dp),end=" ")
print(min(min_dp))