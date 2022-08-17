from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

def topology_sort():
    result = [0] * (N+1)
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append((i, arr[i]))

    while q:
        now, cost = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now]+cost)
            if indegree[i] == 0:
                q.append((i,arr[i]))
    print(result[W]+arr[W])

for _ in range(T):
    N, K = map(int, input().split())
    arr = [0]+list(map(int, input().split()))
    indegree = [0] * (N+1)
    graph = [[] for i in range(N+1)]

    for i in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())
    topology_sort()
