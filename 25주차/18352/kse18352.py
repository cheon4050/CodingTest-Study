#pypy3
from collections import deque

n,m,k,x = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited = [-1]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)


def bfs (start):
    q=deque([start])
    visited[start]=0

    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i]==-1:
                visited[i]=visited[now]+1
                q.append(i)

bfs(x)
flag = False

for i in range(1,n+1):
    if visited[i]==k:
        print(i)
        flag = True #거리가 k인 노드가 하나라도 존재함

if not flag:
    print('-1')

