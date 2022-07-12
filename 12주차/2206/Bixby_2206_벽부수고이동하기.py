import sys
from collections import deque

def bfs():
    q=deque([(0,0,False)])
    visited[0][0][False]=1

    while q:
        x,y,isWallBroken=q.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][isWallBroken]
        for i in range(4):
            nx=x+ dx[i]
            ny=y+ dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][isWallBroken]==0:
                if space[nx][ny]==0:
                    q.append((nx,ny,isWallBroken))
                    visited[nx][ny][isWallBroken]=visited[x][y][isWallBroken]+1

                if not isWallBroken and space[nx][ny]==1:
                    q.append((nx,ny,1))
                    visited[nx][ny][1]=visited[x][y][isWallBroken]+1
    return -1

input=sys.stdin.readline
n,m=map(int,input().split())
space=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[[0]*2 for _ in range(m)]for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs())