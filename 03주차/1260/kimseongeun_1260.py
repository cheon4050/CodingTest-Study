n,m,start = map(int, input().split())
lines=[[0 for z in range(n+1)] for w in range(n+1)]
for i in range(m):
    a,b=map(int, input().split())
    lines[a][b] = lines[b][a] = 1
dfsvisited =[0 for i in range(n+1)]
bfsvisited =[0 for i in range(n+1)]
dfslist=[]
bfslist=[]

def dfs(x):
    dfsvisited[x]=1
    dfslist.append(x)
    for i in range (1, n+1):
        if dfsvisited[i] == 0 and lines[x][i] == 1:
            dfs(i)

def bfs(x):
    q=[x]
    bfsvisited[x] =1
    while q:
        x=q.pop(0)
        bfslist.append(x)
        for i in range(1, n+1):
            if bfsvisited[i]==0 and lines[x][i] == 1:
                q.append(i)
                bfsvisited[i] = 1

dfs(start)
bfs(start)
print(*dfslist)
print(*bfslist)

#dfs는 첫번째 이웃으로 이동하고 나서, 해당 이윳을 기준삼아 다시 또 첫번째 이웃으로 이동하고 동일하게 계속
#진행하여 더이상 연결이 되지 않을 때까지 진행하고 돌아와 두번째 이웃으로 진행

# BFS는 ㅌ첫번째 기점에서 연결된 모든 이웃을 탐색한 후에 첫번째 이웃에서 같은 작업을 반본