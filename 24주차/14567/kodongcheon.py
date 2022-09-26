from collections import deque
import sys
input = sys.stdin.readline
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append((i,1))
    while q:
        now, cnt = q.popleft()
        result.append((now,cnt))
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append((i, cnt+1))
    return result


v, e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[]for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

    indegree[b] += 1

result = topology_sort()
result.sort()
for i in result:
    print(i[1], end = " ")
