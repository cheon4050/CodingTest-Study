m=' '+input()
n=' '+input()
dp=[[0] * (len(n)) for i in range(len(m))]

for i in range(1,len(m)):
    for j in range(1,len(n)):
        dp[i][j]=dp[i-1][j-1]+1 if m[i]==n[j] else max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])