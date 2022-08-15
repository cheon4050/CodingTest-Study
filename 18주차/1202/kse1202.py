#보석도둑
import heapq

N, K = map(int,input().split())
jew = []
bag = []

for i in range(N):
    jewInfo= list(map(int,input().split()))
    heapq.heappush(jew,jewInfo)
for i in range(K):
    jewInfo= int(input())
    heapq.heappush(bag,jewInfo)

answer = 0
temp =[]

while bag:
    cur_bag = heapq.heappop(bag)

    while jew and cur_bag >= jew[0][0]:
        cur_stone = heapq.heappop(jew)
        heapq.heappush(temp,-cur_stone[1])

    if temp:
        answer += -heapq.heappop(temp)
print(answer)