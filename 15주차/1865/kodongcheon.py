import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

def bf():
    for i in range(N):
        for j in range(len(edges)):
            cur, next_node, cost = edges[j]
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

for _ in range(T):
    N,M,W = map(int, input().split())
    edges = []
    dist = [INF] * (N+1)

    for i in range(M):
        a, b, c = map(int, input().split())
        edges.append((a,b,c))
        edges.append((b,a,c))
    for i in range(W):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))
    if bf():
        print("YES")
    else:
        print("NO")
