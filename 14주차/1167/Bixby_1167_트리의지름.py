from collections import deque


def bfs(start):
    visited = [-1]*(n+1)
    queue = deque([start])
    visited[start] = 0
    maxNodeAndDistance = [0, 0]
    while queue:
        v = queue.popleft()
        for i, c in graph[v]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v]+c
                if maxNodeAndDistance[1] < visited[i]:
                    maxNodeAndDistance = i, visited[i]
    return maxNodeAndDistance


n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    for index, vertex in enumerate(tmp[1:-1:2]):
        graph[tmp[0]].append((vertex, tmp[(index+1)*2]))
node, dist = bfs(1)
node, dist = bfs(node)
print(dist)
