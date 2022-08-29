from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 문제 수 n, 먼푸좋문제 m
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
heap = []
result = []

for _ in range(m):
    a, b = map(int, input().split()) # a는 b보다 먼저 푸는 것이 좋다
    indegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if indegree[i] == 0: # 먼저 풀어야 하는 문제가 없는 경우 먼저 힙에 추가
        heappush(heap, i)

while heap: # 힙이 빌 때 까지 반복
    now = heappop(heap) # 힙에서 하나를 빼서 result에 추가
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1 # 해당 정점과 연결되어 있는 노드에서 진입 차수 개수  - 1
        if indegree[i] == 0:
            heappush(heap, i)

print(*result)