from collections import deque


def bfs():
    visited = [False]*(n+1)
    queue = deque([1])
    v = queue.popleft()
    while queue:
        if visited[v]:


n, m = map(int, input().split())
graph = [[]*(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
