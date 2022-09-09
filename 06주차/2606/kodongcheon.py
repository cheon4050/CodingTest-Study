import sys

input = sys.stdin.readline

def DFS(visited, v, graph):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(visited,i, graph)

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(visited, 1, graph)
print(sum(visited)-1)