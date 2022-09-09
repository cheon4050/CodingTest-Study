import sys
from collections import deque

#dfs메서드 정의
def dfs(v):
    #현재 노드를 방문 처리
    visited[v] =True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
#bfs메서드 정의
def bfs(start):
    #queue 구현을 위해 deque 라이브러리 사용
    queue=deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 원소 하나를 뽑아 출력
        v=queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,n+1):
    graph[i].sort()
#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*(n+1)
dfs(v),print()

visited = [False]*(n+1)

bfs(v)