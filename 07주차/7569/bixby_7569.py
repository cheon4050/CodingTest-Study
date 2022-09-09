from collections import deque

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):#6방향
            nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]

            if 0<=nx<h and 0<=ny<n and 0<=nz<m and boxes[nx][ny][nz]==0: #좌표 범위 안에 있고 안익었으면(안익었고 방문 안했으면)
                boxes[nx][ny][nz]=boxes[x][y][z]+1#1일추가
                queue.append((nx,ny,nz))


m,n,h=map(int, input().split())
boxes=[[list(map(int,input().split()))for _ in range(n)]for _ in range(h)]

dx=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

day=0
queue=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k]==1:#익은 토마토는 큐에 넣기
                queue.append((i,j,k))

bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k]==0:#안익은 토마토 있으면
                print(-1)
                exit()
            day=max(day,boxes[i][j][k])
print(day-1)