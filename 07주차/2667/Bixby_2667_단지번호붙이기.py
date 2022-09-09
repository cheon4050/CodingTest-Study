def dfs(x,y):
    if 0<=x<n and 0<=y<n and m[x][y]==1:
        m[x][y]=0
        global cnt
        cnt+=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)
        return True
    return False

n=int(input())
m=[list(map(int,input()))for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
res=[]
cnt=0
for x in range(n):
    for y in range(n):
        if dfs(x,y)==True:
            res.append(cnt)
            cnt=0
print(len(res),*sorted(res),sep="\n")