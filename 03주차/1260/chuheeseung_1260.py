import sys
from collections import deque

def dfs(n):
    visited[n] = True # 방문하면 true로 변경해서 지나갔다는 표시
    print(n, end=' ')

    for i in graph[n]: # n값과 연결된 노드로 이동
        if not visited[i]: # 방문하지 않았으면 dfs 호출하는 과정 반복
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue: # queue가 빌 때까지 반복
        v = queue.popleft() # 왼쪽꺼 하나를 뽑음
        print(v, end=' ')

        for i in graph[v]: # 방문하지 않은 곳 탐색
            if not visited[i]: # 인접한 노드에서 방문하지 않은 곳 발견하면
                queue.append(i) # queue에 추가
                visited[i] = True # 방문했다는 표시


N, M, V = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split()) # 간선이 연결하는 두 정점의 번호
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1): # 정렬 먼저
    graph[i].sort()

visited = [False] * (N + 1) # 먼저 false로 넣음

dfs(V)

print()
visited = [False] * (N + 1)

bfs(V)