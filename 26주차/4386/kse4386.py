import heapq

n = int(input())

star = [list(map(float, input().split())) for _ in range(n)]
edge = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        distance = ((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5
        edge[i].append([distance, j])
        edge[j].append([distance, i])
chk = [False] * n
heap = [[0, 0]]
rs = 0

while heap:

    w, node = heapq.heappop(heap)
    if chk[node] == False:
        chk[node] = True
        rs += w

        for e in edge[node]:
            if chk[e[1]] == False:
                heapq.heappush(heap, e)

print(round(rs, 2))