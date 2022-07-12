import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 방향이 없는 그래프라서 둘 다 추가
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n + 1) # 거리를 측정하는 리스트
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        len, node = heapq.heappop(hq)

        if len > distance[node]: # 지금까지의 거리가 distance[node]보다 크면
            continue # 최솟값을 구하는 것이므로 볼 필요가 없음

        for next_node, val in graph[node]: # node가 갈 수 있는 다른 node값, 거리를 확인
            if distance[next_node] > distance[node] + val:
                # 다음에 갈 노드의 현재까지 최소 거리값 > 현재 노드까지 온 거리 + 다음 노드까지 갈 거리
                distance[next_node] = distance[node] + val # 현재 노드까지 온 거리 + 다음노드까지 갈 거리로 변경
                heapq.heappush(hq, (distance[next_node], next_node)) # heap에 넣어준다

    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n) # 1 -> v1 -> v2 -> n
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n) # 1 -> v2 -> v1 -> n

if path1 >= INF and path2 >= INF: # 내가 설정한 INF 값을 넘을 수 있는 경우가 있어서
    print(-1)
else:
    print(min(path1, path2))