import heapq

inf = float('inf')

# dijkstra
def dijkstra(start, g, n):
    # 최소 비용 배열
    d = [inf] * (n+1)
    d[start] = 0

    # 최소 힙
    mheap = []
    heapq.heappush(mheap, [0,start])

    while mheap:
        tmp = heapq.heappop(mheap)
        cost = tmp[0]
        node = tmp[1]

        if cost > d[node]:
            continue

        for n in g[node]:
            neighbor = n[0]
            n_cost = d[node] + n[1]

            if  n_cost < d[neighbor]:
                d[neighbor] = n_cost
                heapq.heappush(mheap, [n_cost,neighbor])
    return d

# mainㅌ
n, e = [int(x) for x in input().split()]

# 인접리스트
g = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = [int(x) for x in input().split()]
    # 무방향 그래프로 양쪽 모두 추가
    g[a].append([b,c])
    g[b].append([a,c])

v1, v2 = [int(x) for x in input().split()]

d_start = dijkstra(1,g,n)
d_v1 = dijkstra(v1,g,n)
d_v2 = dijkstra(v2,g,n)

answer = min(d_start[v1] + d_v1[v2] + d_v2[n], d_start[v2] + d_v2[v1] + d_v1[n])
print(answer if answer != inf else -1)