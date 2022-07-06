n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
INF = 10e9
graph = [[INF] * n for i in range(n)] # 최소비용을 구하는 문제니까 INF로 초기화

for _ in range(m):
    start, end, distance = map(int, input().split())

    if graph[start-1][end-1] > distance: # 작은 값으로 갱신해서 배열에 넣어주기
        graph[start-1][end-1] = distance

# 플로이드 와샬 알고리즘 : j->k 갈 때 i 거쳐서 가는 경우와 바로 가는 경우 비교해서 작은 값으로 갱신
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k] > graph[j][i] + graph[i][k] and j != k:
                graph[j][k] = graph[j][i] + graph[i][k]

for i in range(n): # INF로 있으면 방문하지 않은 것이라서 0으로 갱신
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(n):
    print(*graph[i])

# 플로이드 와샬 알고리즘
