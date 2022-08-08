import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
course = [[0, 0] for i in range(n+1)]

def dijkstra(graph, start, distance, course):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    course[start].append(start)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                course[i[0]]= course[now] + [i[0]]
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            elif cost == distance[i[0]] and now < course[i[0]][-2]:
                course[i[0]] = course[now] + [i[0]]
                heapq.heappush(q, (cost, i[0]))


dijkstra(graph, start, distance, course)

print(distance[end])
print(len(course[end])-2)
print(*course[end][2:])