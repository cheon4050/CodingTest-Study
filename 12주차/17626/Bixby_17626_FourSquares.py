n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1):
    j=1
    minValue=4
    while j**2<=i:
        minValue=min(minValue,dp[i-j**2]+1)
        j+=1
    dp[i]=minValue
print(dp[n])