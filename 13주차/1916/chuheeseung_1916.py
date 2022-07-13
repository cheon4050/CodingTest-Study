import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
bus = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m): # 버스의 정보 저장
    s, e, c = map(int, input().split())
    bus[s].append((e, c))

start, end = map(int, input().split())

def dijkstra(bus, start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        weight, now = heapq.heappop(q)

        if distance[now] < weight:
            continue

        for i in bus[now]:
            cost = weight + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(bus, start, distance)
print(distance[end])
