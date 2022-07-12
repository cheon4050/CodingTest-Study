import heapq

n, m, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
result = -1

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    # [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], []]

def dijkstra(s, e):
    hq = []
    dist = [INF for _ in range(n + 1)] # 거리 계산하는 리스트를 INF로 초기화
    heapq.heappush(hq, (0, s))
    dist[s] = 0 # 시작 노드 거리 계산 (자신은 0)

    while hq:
        distance, now = heapq.heappop(hq)

        if dist[now] < distance:
            continue

        for next in graph[now]: # 해당 노드의 인접한 노드들 간의 거리 계산
            cost = distance + next[1] # s->now 거리 + now->now인접노드 거리

            if cost < dist[next[0]]: # cost < s->now인접노드 다이렉트 거리
                dist[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))

    return dist[e]

for i in range(1, n + 1):
    _dijkstra = dijkstra(i, x) + dijkstra(x, i) # s -> e, e -> s 둘 다 계산
    result = max(result, _dijkstra) # 거리를 max 함수를 통해서 최댓값으로 갱신

print(result)


# 다익스트라 알고리즘 이용
# 가는 최단 시간 경로 + 오는 최단 시간 경로
# 둘 다 구해서 합한 값 중 최댓값을 출력
