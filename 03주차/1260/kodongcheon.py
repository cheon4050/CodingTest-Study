from collections import deque
N, M, V = map(int, input().split())
graph = [[]for i in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
for i in range(1, len(graph)):
    graph[i].sort()
dfsVisited = [False]*(N+1)
bfsVisited = [False]*(N+1)
def DFS(v):
    dfsVisited[v]= True
    print(v, end=" ")
    for i in graph[v]:
        if dfsVisited[i] == True:
            continue
        DFS(i)
def BFS(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        bfsVisited[v] = True
        print(v, end=" ")
        for i in graph[v]:
            if bfsVisited[i] == True or i in queue:
                continue
            queue.append(i)
DFS(V)
print()
BFS(V)