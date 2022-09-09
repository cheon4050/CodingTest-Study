N = int(input())

arr = []
for _ in range(N):
    R, G ,B= map(int, input().split())
    arr.append([R,G,B])

dp = []
dp.append(arr[0])

for i in range(1, N):
    select_R = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    select_G = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    select_B = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    dp.append((select_R,select_G,select_B))

A, B, C = dp[-1]
print(min(A,B,C))