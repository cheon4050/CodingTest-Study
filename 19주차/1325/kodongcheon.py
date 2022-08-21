import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    visited2 = [False] * (N + 1)
    q = deque([v])
    cnt = 0
    while q:
        v = q.popleft()
        visited2[v] = True
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                q.append(i)
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
count = [0] * (N+1)
result = []
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
for i in range(1, N+1):
    if not visited[i]:
        count[i] = bfs(i)
check = max(count)
for i in range(1,N+1):
    if count[i] == check:
        result.append(i)
print(*result, sep= " ")