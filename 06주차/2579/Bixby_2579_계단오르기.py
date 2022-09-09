n=int(input())
step=[int(input())for _ in range(n)]
dp=[0]*n

if n<3:
    print(sum(step))
else:
    dp[0]=step[0]
    dp[1]=step[0]+step[1]
    dp[2]=max(step[0]+step[2],step[1]+step[2])

    for i in range(3,n):
        dp[i]=max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])
    print(dp[-1])