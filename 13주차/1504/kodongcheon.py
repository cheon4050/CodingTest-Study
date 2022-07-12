import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m= map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())
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

distanceV = [INF] * (n+1)
distanceV1 = [INF] * (n+1)
distanceV2 = [INF] * (n+1)

dijkstra(graph, 1, distanceV)
dijkstra(graph, v1, distanceV1)
dijkstra(graph, v2, distanceV2)

result = min(distanceV[v1]+distanceV1[v2]+distanceV2[n], distanceV[v2]+distanceV2[v1]+distanceV1[n])
if result >=INF:
    print(-1)
else:
    print(result)