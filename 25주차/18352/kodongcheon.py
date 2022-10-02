import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

INF = int(1e9)
distance = [INF] * (N+1)

def bfs(v, graph, distance):
    distance[v] = 0
    q = deque([(v, 0)])
    while q:
        x, cost = q.popleft()
        for i in graph[x]:
            if distance[i] == INF:
                q.append((i, cost+1))
                distance[i] = cost+1
bfs(X, graph, distance)

result = []

for i in range(1,N+1):
    if distance[i] == K:
        result.append(i)

if result:
    for i in result:
        print(i)
else:
    print(-1)






