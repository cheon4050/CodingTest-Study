#어떤 임의의 정점을 선택해 출발했을 때 음수 사이클에 도달할 수 없는 경우가 생길 수 있다는 점
# 한번이라도 방문한 정점에 대해서만 최단거리를 갱신하는 경우
#   모든 최단거리를 0으로 초기화시켜 모든 정점에서 동시에 시작하도록 조정
#   어떤 가짜 정점 N+1을 만들고 모든 정점에 가중치 0으로 연결되도록 한 후 N+1에서 시작하면 모든 정점에 도달할 수 있으므로 음수 사이클에 무조건 도달 가능
# /모든 정점에 대해 최단거리를 갱신하는 경우
INF = 5000 * 10000

T = int(input())


def BF_AllNode(N, G):
    dist = [INF] * (N + 1)

    #시작지점 1번에서 출발
    dist[1] = 0

    for _ in range(1, N + 1):
        for i in range(1, N + 1):
            for j in G[i]:
                if dist[j[0]] > dist[i] + j[1]:
                    dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 1):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


def BF_ZeroNode(N, G):
    dist = [0] * (N + 1)

    #시작지점 1번에서 출발
    dist[1] = 0

    for _ in range(1, N + 1):
        for i in range(1, N + 1):
            for j in G[i]:
                if dist[i] == INF:
                    continue
                else:
                    if dist[j[0]] > dist[i] + j[1]:
                        dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 1):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


def BF_AnotherNode(N, G):
    dist = [0] * (N + 1)

    temp = [(i, 0) for i in range(1, N + 1)]
    G.insert(N + 1, temp)

    #시작지점 N+1번(가짜 노드)에서 출발
    dist.append(0)

    for _ in range(1, N + 2):
        for i in range(1, N + 2):
            for j in G[i]:
                if dist[i] == INF:
                    continue
                else:
                    if dist[j[0]] > dist[i] + j[1]:
                        dist[j[0]] = dist[i] + j[1]

    isMinusCycle = False

    for i in range(1, N + 2):
        for j in G[i]:
            if dist[i] == INF:
                continue
            else:
                if dist[j[0]] > dist[i] + j[1]:
                    isMinusCycle = True

    if isMinusCycle:
        print("YES")
    else:
        print("NO")


for _ in range(T):
    N, M, W = map(int, input().split())

    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = map(int, input().split())

        G[S].append((E, T))
        G[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())

        G[S].append((E, -1 * T))

    BF_AnotherNode(N, G)