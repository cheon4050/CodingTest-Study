from collections import deque
import sys
input = sys.stdin.readline
V = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(V):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp)-2, 2):
        graph[temp[0]].append((temp[i], temp[i+1]))

def bfs(graph, start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (V+1)
    visited[start] = True
    max_result = 0
    index = 0
    while q:
        v, cnt = q.popleft()
        for i in graph[v]:
            if not visited[i[0]]:
                q.append((i[0], cnt+i[1]))
                visited[i[0]] = True
        max_result = max(max_result, cnt)
        if max_result == cnt:
            index = v
    return index, max_result

index, max_result = bfs(graph, 1)
index, max_result = bfs(graph, index)
print(max_result)
