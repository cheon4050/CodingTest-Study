import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
result = []
graph = [[]for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1,N+1):
    visited = [0]*(N+1)
    queue = deque()
    queue.append(i)
    while(queue):
        x = queue.popleft()
        for j in graph[x]:
            if visited[j] == 0 and j != i:
                visited[j] = visited[x] + 1
                queue.append(j)
    result.append((i,sum(visited)))
print(min(result, key=lambda x: x[1])[0])




