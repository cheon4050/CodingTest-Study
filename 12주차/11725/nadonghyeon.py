import sys
sys.setrecursionlimit(10**9)

def dfs(V):
    visited[V]=True
    for i in graph[V]:
        if not visited[i]:
            answer[i]=V
            dfs(i)

N=int(input())

graph=[[] for _ in range(N+1)]
visited=[False for _ in range(N+1)]
answer=[1 for _ in range(N+1)]

for i in range(N-1):
    A,B=map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

#↓방문 순서를 확인할 필요없고 부모 노드만 확인하면 되기때문에 생략해도 상관x
for i in graph:
    i.sort()

dfs(1)

for i in range(2,len(answer)):
    print(answer[i])