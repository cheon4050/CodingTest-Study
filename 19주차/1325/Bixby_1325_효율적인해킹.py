import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [False]*(n+1)
    count = 1
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count


n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_count = 1
computer_list = []

for i in range(1, n+1):
    count = bfs(i)

    if count > max_count:
        max_count = count
        computer_list.clear()
        computer_list.append(i)
    elif count == max_count:
        computer_list.append(i)

print(*computer_list)
