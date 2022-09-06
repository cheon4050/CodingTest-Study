N, K = list(map(int, input().split())) #N 명의 원생, K 개의 조

keys = []
arr_K = [[]for _ in range(K)]
h =input().split()


K_count = []
remainder = int(N % K) #남는 원생들

for i in range(0,K):
    K_count.append(N//K) #조 개수로 K_count 초기화
for i in range(remainder):
    K_count[i]+=1 # 거기에 남는 원생들 1명씩 추가

j=0
for i in range(0,K):
    for val in range(0,K_count[i]):
        arr_K[i].append(h[j])
        j+=1
costs=[]
for i in range(1,N):
    costs.append(int(h[i])-int(h[i-1]))
costs.sort()
sum_count = 0

sum = 0
for i in range(K):
    sum_count += len(arr_K[i])-1
for i in range(0,sum_count):
    sum+=costs[i]

# print("arr_K : ",arr_K)
# print("sum : ", sum)
# print(costs)
print(sum)