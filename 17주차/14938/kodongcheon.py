import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int,input().split())

arr = [0] + list(map(int,input().split()))
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if graph[i][j] <=m:
            temp += arr[j]
    result = max(result, temp)
print(result)

