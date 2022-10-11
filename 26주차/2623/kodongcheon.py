from collections import deque

v, e = map(int, input().split())

indegree = [0]*(v+1)

graph = [[]for i in range(v+1)]

for _ in range(e):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] +=1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if not sum(indegree):
        for i in result:
            print(i)
    else:
        print(0)

topology_sort()