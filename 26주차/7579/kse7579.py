n, m=map(int,input().split()) #앱의 개수 n, 확보가 필요한 바이트 m
memory = list(map(int, input().split()))#각 앱의 메모리 바이트
cost= list(map(int, input().split())) #각 앱을 비활성화 했을 경우의 비용
data=[]

for i in range(0,n):
    data.append([memory[i],cost[i]])
cost_sum=sum(cost) # 전체
# print(cost_sum)
dp=[0]*(cost_sum+1)
for app in data:
    for i in range(cost_sum, app[1]-1, -1):
        dp[i]=max(dp[i], dp[i-app[1]]+app[0])
# for i in range(len(dp)):
#     print(i,"번째", dp[i])

for i in range(cost_sum+1):
    if dp[i] >= m:
        print(i, end='')
        break

# n, m=map(int,input().split()) #앱의 개수 n, 확보가 필요한 바이트 m
# memory = list(map(int, input().split()))#각 앱의 메모리 바이트
# cost= list(map(int, input().split())) #각 앱을 비활성화 했을 경우의 비용
# dp=[]
#
# for i in range(0,n):
#     dp.append([memory[i], cost[i]])
# dp.sort()
# sum=0
# cost_sum=0
# for app in dp:
#     sum+=app[0]
#     cost_sum+=app[1]
#     if sum>=m:
#         break
#
# print(cost_sum)