INF = int(1e9) #maxsize 설정

# 노드의 개수 및 간선의 개수 입력받음
n = int(input())
m = int(input())
# 2차원 리스트 (그래프 표현)을 만들고 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 간선에서 노선의 최소값을 저장한다.
    if graph[a][b] > c:
        graph[a][b] = c

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            # a -> b와 a -> k -> b까지의 최소 값을 구한다. 즉, 거리가 짧은 거를 구함
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INF)이라고 출력
        if graph[a][b] == INF:
            print(0, end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()