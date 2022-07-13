import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance2 = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph2[b].append((a,c))

def dijkstra(graph, start, distance):
    q = []
    heapq .heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(graph, start, distance)
dijkstra(graph2, start, distance2)

result = 0
for i in range(1, n+1):
    result = max(result , distance[i]+distance2[i])
print(result)
