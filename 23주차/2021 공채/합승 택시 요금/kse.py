# 합승택시요금
import heapq

def dijkstra(s, adj):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        d, u = heapq.heappop(q)
        if dist[u] < d:
            continue
        for v, dv in adj[u]:
            if dist[v] > dist[u] + dv:
                dist[v] = dist[u] + dv
                heapq.heappush(q, (dist[v], v))

    return dist


def solution(n, s, a, b, fares):
    answer = float('inf')
    adj = [[] for _ in range(n+1)]
    for fare in fares:
        adj[fare[0]].append((fare[1], fare[2]))
        adj[fare[1]].append((fare[0], fare[2]))

    s_dist = dijkstra(s, adj) # s에서 모든 지점까지의 최단 거리
    a_dist = dijkstra(a, adj) # a에서 모든 지점까지의 최단 거리
    b_dist = dijkstra(b, adj) # b에서 모든 지점까지의 최단 거리

    # i번째 지점에서 a,b,s까지의 최소 거리 갱신
    for i in range(1, n+1):
        answer = min(answer, s_dist[i] + a_dist[i] + b_dist[i])

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))