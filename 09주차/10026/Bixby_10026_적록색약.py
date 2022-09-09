from collections import deque
def bfs(Chart):
    visited=[[False for _ in range(n)]for _ in range(n)]
    q=deque([])
    cnt=0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                q.append((i,j,display[i][j]))
                cnt+=1
                while q:
                    x,y,color=q.popleft()
                    visited[x][y]=True
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<n and Chart[display[nx][ny]]==Chart[color] and not visited[nx][ny]:
                            #범위 안에 있고, 색이 같고, 방문하지 않았으면
                            q.append((nx,ny,display[nx][ny]))
                            visited[nx][ny]=True
    return cnt

n=int(input())
display=[input()for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
normal={'R':0,'G':1,'B':2}
colorWeaknes={'R':0,'G':0,'B':2}
print(bfs(normal),bfs(colorWeaknes))