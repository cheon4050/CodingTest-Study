def dfs(v=1): #시작 기본값 1번 컴퓨터
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n=int(input())

graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(int(input())):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
dfs()
print(sum(visited)-1)# 방문개수-1 = 감염된 컴퓨터 -1 = 1번 컴퓨터가 감염시킨 컴퓨터 개수