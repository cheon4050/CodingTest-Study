def diffusion(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if tmp[nx][ny]==0:
                tmp[nx][ny]=2
                diffusion(nx,ny)
def dfs(count=0):
    global ans
    if count==3:
        for i in range(n):
            for j in range(m):
                tmp[i][j]=lab[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    diffusion(i,j)
        safeZone=0
        for i in range(n):
            for j in range(m):
                if tmp[i][j]==0:
                    safeZone+=1
        ans=max(ans,safeZone)
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j]==0:
                lab[i][j]=1
                count+=1
                dfs(count)
                lab[i][j]=0
                count-=1

n,m= map(int, input().split())
lab=[list(map(int,input().split()))for _ in range(n)]
tmp=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans=0                
dfs()
print(ans)