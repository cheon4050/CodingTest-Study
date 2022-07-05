from collections import deque
def bfs(start):
    queue= deque([start])
    visited[start]=True
    while queue:
        v= queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                parent[i]=v #부모 정보 입력

n=int(input())
graph=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
parent=[i for i in range(n+1)] #부모를 자기 자신으로 초기화
bfs(1) #루트가 1이라서
print(*parent[2:]) #2번노드부터 출력