import heapq

n = int(input()) #별의 개수

star = [list(map(float, input().split())) for _ in range(n)] #별의 x, y좌표
edge = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        distance = ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5 #두점사이의 거리
        edge[i].append([distance, j]) #그 거리와 y좌표를 x정보에
        edge[j].append([distance, i]) #그 거리와 x좌표를 y정보에
temp = [0] * n
heap = [[0, 0]]
answer = 0

while heap:
    i, node = heapq.heappop(heap)

    print(i, node)
    if temp[node] == 0:
        temp[node] = 1
        answer += i

        for j in edge[node]:
            if temp[j[1]] == 0:
                heapq.heappush(heap, j)

print(round(answer, 2))