from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
result = [0] * (n+1)

for i in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited[1] = True
while(queue):
    x = queue.popleft()
    for i in graph[x]:
        if not visited[i]:
            result[i] = x
            visited[i] = True
            queue.append(i)
print(*result[2:], sep="\n")



