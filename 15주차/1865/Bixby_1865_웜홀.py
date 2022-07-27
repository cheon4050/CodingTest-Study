import sys
INF = int(1e9)
input = sys.stdin.readline


def has_negative_cycle():
    dist[1] = 0
    for i in range(n):
        for node in range(1, n+1):
            for next_node, next_cost in graph[node]:
                if dist[next_node] > dist[node] + next_cost:
                    dist[next_node] = dist[node] + next_cost
                    if i == n-1:
                        return True
    return False


for _ in range(int(input())):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)

    # 도로 입력 받기 (양방향)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])

    # 웜홀 입력 받기 (단방향)
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    print("YES" if has_negative_cycle() else "NO")
