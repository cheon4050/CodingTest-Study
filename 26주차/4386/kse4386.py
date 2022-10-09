import heapq

n = int(input()) #별의 개수

star = [list(map(float, input().split())) for _ in range(n)] #별의 x, y좌표
edge = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        distance = ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5
        edge[i].append([distance, j])
        edge[j].append([distance, i])
temp = [False] * n
heap = [[0, 0]]
answer = 0

while heap:

    i, node = heapq.heappop(heap)
    if temp[node] == False:
        temp[node] = True
        answer += i

        for j in edge[node]:
            if temp[j[1]] == False:
                heapq.heappush(heap, j)

print(round(answer, 2))