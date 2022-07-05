import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().rstrip())))
def bfs(arr, v, visited):
    queue = deque([(v[0],v[1],1)])
    visited[v[0]][v[1]] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while(queue):
        a = queue.popleft()
        for i in range(4):
            x = a[0]+dx[i]
            y = a[1]+dy[i]
            if 0<=x < N and 0<=y<M and visited[x][y] ==0:
                if arr[x][y] != 1:
                    queue.append((x,y,a[2]+1))
                visited[x][y] = a[2]+1
distance1 = [[0]*M for i in range(N)]
distance2 = [[0]*M for i in range(N)]
bfs(arr,[0,0],distance1)
bfs(arr,[N-1,M-1],distance2)
result = 10000000
for i in range(N):
    for j in range(M):
        if distance1[i][j] != 0 and distance2[i][j] != 0:
            result = min(result,distance1[i][j]+distance2[i][j]-1)
if result == 10000000:
    print(-1)
else:
    print(result)


