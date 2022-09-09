def bfs(x=0,y=0):#시작 기본값 (0,0)
    q = deque([(x,y)])
    while q: #큐가 빌때까지
        x,y=q.popleft()
        for i in range(4):#상하좌우 탐색
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<n) and (0<=ny<m) and maze[nx][ny]==1: #좌표 범위 안이고, 처음 방문하는 이동할 수 있는 칸이라면
                maze[nx][ny]=maze[x][y]+1 #지나온 칸의 개수+1
                q.append((nx,ny))
    return maze[n-1][m-1] #출구에 도착했을때 지나온 칸의 개수 반환

from collections import deque

n,m=map(int,input().split())
maze=[(list(map(int,input()))) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs())